"""End-to-end deterministic RDF/OWL to OKF compilation pipeline."""

from __future__ import annotations

import hashlib
import json
import platform
import re
import subprocess
from collections import Counter
from pathlib import Path

import rdflib
import yaml

from . import __version__
from .ingestion import load_rdf_sources
from .profiles import get_profile
from .projection import project
from .rendering import write_bundle
from .semantic_builder import build_semantic_model
from .validation.okf import validate_projection


def _source_revision(source: Path) -> str | None:
    directory = source if source.is_dir() else source.parent
    try:
        result = subprocess.run(
            ["git", "-C", str(directory), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def _fibo_release(version_iris: list[str], revision: str | None, override: str | None) -> str:
    if override:
        return override
    dates = [date for iri in version_iris for date in re.findall(r"/(\d{8})/", iri)]
    if dates:
        return max(dates)
    if revision:
        return f"git-{revision[:12]}"
    return "unversioned"


def _profile_digest(profile) -> str:
    if hasattr(profile, "config"):
        serialized = yaml.safe_dump(profile.config, sort_keys=True, allow_unicode=True)
    else:
        serialized = json.dumps({"name": profile.name, "version": profile.version}, sort_keys=True)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def _domain(entity_iri: str, namespace: str = "https://spec.edmcouncil.org/fibo/ontology/") -> str | None:
    if not entity_iri.startswith(namespace):
        return None
    parts = entity_iri[len(namespace):].split("/")
    if parts and re.fullmatch(r"\d{8}", parts[0]):
        parts = parts[1:]
    if not parts or not re.fullmatch(r"[A-Z][A-Z0-9_-]*", parts[0]):
        return None
    return parts[0]


def _write_report(path: Path, report: dict) -> None:
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def compile_ontology(
    source: str | Path,
    output: str | Path,
    *,
    profile_name: str = "fibo",
    scope: str = "all",
    catalog: str | Path | None = None,
    fibo_version: str | None = None,
) -> dict:
    """Compile local RDF/OWL sources to an OKF 0.2 bundle or set of bundles.

    Inputs are parsed offline. An OASIS XML catalog resolves imports; remote
    documents and remote JSON-LD contexts are never fetched.
    """
    source_path = Path(source).expanduser().resolve()
    output_path = Path(output).expanduser().resolve()
    if not source_path.exists():
        raise FileNotFoundError(f"RDF source does not exist: {source_path}")
    if output_path.exists():
        raise FileExistsError(f"Output already exists; choose a new path: {output_path}")

    profile = get_profile(profile_name)
    loaded = load_rdf_sources(source_path, catalog=catalog, output=output_path)
    model = build_semantic_model(loaded.graph, loaded.origins, loaded.sources)
    model.warnings.extend(loaded.warnings)
    model.imports = loaded.imports
    revision = _source_revision(source_path)
    release = _fibo_release(model.version_iris, revision, fibo_version)
    if not re.fullmatch(r"[A-Za-z0-9._-]+", release):
        raise ValueError("Source version must contain only letters, digits, dots, underscores, and hyphens")

    selected_scope = scope.lower()
    if selected_scope == "domains":
        if profile.name != "fibo":
            raise ValueError("The domains scope is available only for the FIBO profile")
        scopes = sorted({domain for iri, entity in model.entities.items() if profile.select(entity) if (domain := _domain(iri))})
    elif selected_scope == "all":
        scopes = ["all"]
    else:
        scopes = [scope.upper()]

    output_path.mkdir(parents=True, exist_ok=False)
    profile_digest = _profile_digest(profile)
    results = []
    validation_errors = []
    quality_warnings = []
    try:
        for bundle_scope in scopes:
            projection = project(model, profile, scope=bundle_scope)
            bundle_name = f"{profile.name}-{release}-{bundle_scope.lower()}-okf-0.2"
            bundle_path = output_path / bundle_name
            write_bundle(
                bundle_path,
                projection,
                model,
                loaded.locations,
                release=release,
                source_revision=revision,
                profile_digest=profile_digest,
                python_version=platform.python_version(),
                dependency_versions={"rdflib": rdflib.__version__, "PyYAML": yaml.__version__},
            )
            # write_bundle copies provenance files based on the profile scope.
            validation = validate_projection(projection, bundle_path)
            validation_errors.extend({**item, "bundle": bundle_name} for item in validation.conformance_errors)
            quality_warnings.extend({**item, "bundle": bundle_name} for item in validation.quality_warnings)
            results.append({"name": bundle_name, "path": bundle_name, "scope": bundle_scope, "projected_entities": len(projection.documents)})

        entity_counts = Counter(entity.kind for entity in model.entities.values())
        projected_counts = Counter()
        for result in results:
            projection_scope = result["scope"]
            for iri, entity in model.entities.items():
                if profile.select(entity) and (projection_scope == "all" or _domain(iri) == projection_scope.upper()):
                    projected_counts[entity.kind] += 1
        report = {
            "source": {
                "path": source_path.name if source_path.is_file() else ".",
                "fibo_version": release,
                "git_revision": revision,
                "files": [
                    {"path": item.path, "format": item.format, "sha256": item.sha256}
                    for item in model.source_files
                ],
                "imports": model.imports,
                "unresolved_imports": [item for item in loaded.warnings if item["code"] == "IMPORT_UNRESOLVED_OFFLINE"],
            },
            "compiler": {
                "name": "owl2okf",
                "version": __version__,
                "profile": profile.name,
                "profile_version": profile.version,
                "profile_sha256": profile_digest,
                "python_version": platform.python_version(),
                "dependencies": {"rdflib": rdflib.__version__, "PyYAML": yaml.__version__},
                "reasoning": "asserted",
                "configuration": {"scope": scope, "offline": True, "catalog": Path(catalog).name if catalog else "catalog-v001.xml"},
            },
            "statistics": {
                "triples": model.triple_count,
                "entities_discovered": sum(entity_counts.values()),
                "entities_discovered_by_kind": dict(sorted(entity_counts.items())),
                "entities_projected": sum(result["projected_entities"] for result in results),
                "entities_projected_by_kind": dict(sorted(projected_counts.items())),
                "unsupported_constructs": dict(sorted(model.unsupported.items())),
            },
            "bundles": results,
            "validation": {
                "okf_0_2_conformance_errors": validation_errors,
                "quality_warnings": quality_warnings,
                "source_and_semantic_warnings": model.warnings,
            },
        }
        _write_report(output_path / "conversion-report.json", report)
        if validation_errors:
            raise ValueError(f"Generated bundles have {len(validation_errors)} OKF 0.2 conformance errors; see conversion-report.json")
    except Exception:
        # Keep the report and any generated bundle on failure for diagnosis.
        if not (output_path / "conversion-report.json").exists():
            _write_report(output_path / "conversion-report.json", {"error": "conversion interrupted; inspect the command output"})
        raise
    return report
