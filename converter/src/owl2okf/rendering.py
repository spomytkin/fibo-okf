"""Write deterministic Markdown/YAML bundles from an OKF projection."""

from __future__ import annotations

import json
import re
import shutil
from collections import Counter
from pathlib import Path, PurePosixPath

import yaml

from . import __version__
from .profiles.base import OntologyProfile
from .projection import OKFProjection
from .semantic import OntologyModel


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def _markdown_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("\n", " ").replace("\r", " ")


def _directory_indexes(projection: OKFProjection, bundle: Path) -> None:
    documents_by_directory: dict[PurePosixPath, list] = {}
    directories: set[PurePosixPath] = set()
    for document in projection.documents.values():
        path = PurePosixPath(document.path)
        directory = path.parent
        documents_by_directory.setdefault(directory, []).append(document)
        while directory != PurePosixPath("."):
            directories.add(directory)
            directory = directory.parent
    children_by_parent: dict[PurePosixPath, set[PurePosixPath]] = {}
    for directory in directories:
        children_by_parent.setdefault(directory.parent, set()).add(directory)

    for directory in sorted(directories, key=lambda item: (len(item.parts), item.as_posix())):
        entries = []
        children = sorted(
            children_by_parent.get(directory, set()),
            key=lambda item: item.name.casefold(),
        )
        for child in children:
            entries.append(f"* [{_markdown_text(child.name)}]({child.name}/)")
        for document in sorted(documents_by_directory.get(directory, []), key=lambda item: item.path.casefold()):
            title = str(document.frontmatter["title"])
            entries.append(f"* [{_markdown_text(title)}]({PurePosixPath(document.path).name})")
        _write_text(bundle / directory / "index.md", "# Concepts\n\n" + "\n".join(entries))

    top_directories = sorted({PurePosixPath(document.path).parts[0] for document in projection.documents.values()}, key=str.casefold)
    root_entries = [f"* [{_markdown_text(PurePosixPath(item).name)}]({item}/)" for item in top_directories]
    profile_text = f"Profile: `{projection.profile_name} {projection.profile_version}`."
    _write_text(
        bundle / "index.md",
        "---\nokf_version: \"0.2\"\n---\n\n"
        f"# {projection.profile_name.upper()} OKF bundle\n\n"
        f"{profile_text} Open the domain and module indexes below to browse the projected ontology concepts.\n\n"
        "Build files: [conversion log](log.md), [bundle manifest](references/fibo-okf/bundle.json).\n\n"
        "## Concepts\n\n" + "\n".join(root_entries),
    )


def _copy_sources(bundle: Path, source_locations: dict[str, Path], selected: set[str]) -> dict[str, dict[str, str]]:
    manifest = {}
    for name in sorted(selected, key=str.casefold):
        source = source_locations.get(name)
        if source is None or not source.is_file():
            continue
        relative = PurePosixPath(name)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"Unsafe source path in manifest: {name}")
        target = bundle / "references" / "fibo" / Path(*relative.parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        manifest[name] = {"bundle_path": f"references/fibo/{name}"}
    return manifest


def _bundle_manifest(
    projection: OKFProjection,
    model: OntologyModel,
    *,
    release: str,
    source_revision: str | None,
    included_sources: set[str],
    profile_digest: str,
    python_version: str,
    dependency_versions: dict[str, str],
) -> dict:
    source_by_path = {source.path: source for source in model.source_files}
    kinds = Counter(model.entities[iri].kind for iri in projection.entity_paths)
    return {
        "bundle_format": "OKF",
        "okf_version": "0.2",
        "bundle_name": f"fibo-{release}-{projection.scope}-okf-0.2",
        "source": {
            "fibo_version": release,
            "git_revision": source_revision,
            "owl_version_iris": model.version_iris,
            "imports": model.imports,
            "reasoning": "asserted",
            "source_files": [
                {"path": path, "sha256": source_by_path[path].sha256, "format": source_by_path[path].format}
                for path in sorted(included_sources, key=str.casefold)
                if path in source_by_path
            ],
        },
        "compiler": {
            "name": "owl2okf",
            "version": __version__,
            "profile": projection.profile_name,
            "profile_version": projection.profile_version,
            "profile_sha256": profile_digest,
            "python_version": python_version,
            "dependencies": dependency_versions,
        },
        "statistics": {
            "triples": model.triple_count,
            "entities_projected": len(projection.documents),
            "entities_by_kind": dict(sorted(kinds.items())),
            "unsupported_constructs": dict(sorted(model.unsupported.items())),
        },
    }


def write_bundle(
    bundle: Path,
    projection: OKFProjection,
    model: OntologyModel,
    source_locations: dict[str, Path],
    *,
    release: str,
    source_revision: str | None,
    profile_digest: str,
    python_version: str,
    dependency_versions: dict[str, str],
) -> dict:
    if bundle.exists():
        raise FileExistsError(f"Bundle path already exists: {bundle}")
    bundle.mkdir(parents=True)
    for document in projection.documents.values():
        rendered_yaml = yaml.safe_dump(
            document.frontmatter,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=True,
            width=120,
        ).rstrip()
        _write_text(bundle / document.path, f"---\n{rendered_yaml}\n---\n\n{document.body}")

    selected_sources = {
        source_path
        for iri in projection.entity_paths
        for source_path in model.entities[iri].source_paths
    }
    if projection.scope == "all":
        selected_sources.update(source.path for source in model.source_files)
    else:
        selected_sources.update(
            source.path for source in model.source_files
            if "/" not in source.path
            or source.path.split("/", 1)[0].upper() in {projection.scope.upper(), "ETC"}
        )
    selected_sources.update(extra for extra in ("catalog-v001.xml", "LICENSE") if extra in source_locations)
    copied = _copy_sources(bundle, source_locations, selected_sources)
    source_manifest_records = {source.path: source for source in model.source_files}
    for path in copied:
        source = source_manifest_records.get(path)
        if source:
            copied[path]["sha256"] = source.sha256
            copied[path]["format"] = source.format

    manifest = _bundle_manifest(
        projection,
        model,
        release=release,
        source_revision=source_revision,
        included_sources=selected_sources,
        profile_digest=profile_digest,
        python_version=python_version,
        dependency_versions=dependency_versions,
    )
    manifest["source"]["source_files"] = [
        {"path": path, "bundle_path": f"references/fibo/{path}", "sha256": source_manifest_records[path].sha256,
         "format": source_manifest_records[path].format}
        for path in sorted(copied, key=str.casefold)
        if path in source_manifest_records
    ]
    _write_text(
        bundle / "references" / "fibo-okf" / "bundle.json",
        json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True),
    )
    _directory_indexes(projection, bundle)
    date_match = re.search(r"(\d{4})(\d{2})(\d{2})", release)
    log_date = "-".join(date_match.groups()) if date_match else "1970-01-01"
    kinds = Counter(model.entities[iri].kind for iri in projection.entity_paths)
    _write_text(
        bundle / "log.md",
        "# Conversion Log\n\n"
        f"## {log_date}\n\n"
        f"* **Generation**: Projected {len(projection.documents)} entities with `owl2okf {__version__}` and profile `{projection.profile_name} {projection.profile_version}`.\n"
        f"* **Source**: FIBO version `{release}`; source revision `{source_revision or 'unknown'}`.\n"
        f"* **Entities**: {json.dumps(dict(sorted(kinds.items())), sort_keys=True)}.\n",
    )
    return manifest
