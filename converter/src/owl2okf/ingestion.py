"""Deterministic, catalog-backed RDF ingestion with offline import resolution."""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

from rdflib import Dataset, Graph, URIRef
from rdflib.namespace import OWL, RDF

from .semantic import SourceFile

FORMAT_BY_SUFFIX = {
    ".rdf": "xml",
    ".owl": "xml",
    ".ttl": "turtle",
    ".n3": "n3",
    ".nt": "nt",
    ".jsonld": "json-ld",
    ".json": "json-ld",
    ".nq": "nquads",
}
FIBO_CATALOG_NS = "urn:oasis:names:tc:entity:xmlns:xml:catalog"


@dataclass
class LoadedOntology:
    graph: Graph
    origins: dict[URIRef, set[str]]
    sources: list[SourceFile]
    locations: dict[str, Path]
    warnings: list[dict[str, str]]
    imports: list[str]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _catalog_entries(catalog: Path | None) -> dict[str, Path]:
    if catalog is None or not catalog.is_file():
        return {}
    root = ET.parse(catalog).getroot()
    entries = {}
    for element in root.iter():
        if element.tag.rsplit("}", 1)[-1] != "uri":
            continue
        name = element.attrib.get("name")
        target = element.attrib.get("uri")
        if name and target:
            resolved = Path(target)
            if not resolved.is_absolute():
                resolved = (catalog.parent / resolved).resolve()
            entries[name] = resolved
    return entries


def _format(path: Path) -> str:
    try:
        return FORMAT_BY_SUFFIX[path.suffix.lower()]
    except KeyError as exc:
        raise ValueError(f"Unsupported RDF source format: {path.suffix}") from exc


def _relative(path: Path, source_root: Path) -> str:
    try:
        return path.resolve().relative_to(source_root.resolve()).as_posix()
    except ValueError:
        return f"external/{_sha256(path)[:12]}-{path.name}"


def _reject_remote_jsonld_context(path: Path) -> None:
    document = json.loads(path.read_text(encoding="utf-8"))

    def inspect(value: object) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "@context":
                    contexts = child if isinstance(child, list) else [child]
                    for context in contexts:
                        if isinstance(context, str) and urlsplit(context).scheme in {"http", "https"}:
                            raise ValueError(
                                f"Remote JSON-LD context is blocked in offline mode: {context}. "
                                "Inline the context or provide a local catalog mapping."
                            )
                        inspect(context)
                else:
                    inspect(child)
        elif isinstance(value, list):
            for child in value:
                inspect(child)

    inspect(document)


def _source_files(source: Path, output: Path) -> list[Path]:
    if source.is_file():
        _format(source)
        return [source]
    output = output.resolve()
    paths = []
    for path in source.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in FORMAT_BY_SUFFIX:
            continue
        if any(part.startswith(".") for part in path.relative_to(source).parts):
            continue
        try:
            path.resolve().relative_to(output)
            continue
        except ValueError:
            pass
        paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(source).as_posix().casefold())


def load_rdf_sources(source: str | Path, *, catalog: str | Path | None = None, output: str | Path | None = None) -> LoadedOntology:
    """Load local RDF files and resolve owl:imports through an OASIS XML catalog.

    Network access is never used. JSON-LD remote contexts are rejected so an
    input cannot silently fetch mutable context documents during a build.
    """
    root = Path(source).expanduser().resolve()
    output_path = Path(output).expanduser().resolve() if output else root / "__no_output__"
    source_root = root if root.is_dir() else root.parent
    catalog_path = Path(catalog).expanduser().resolve() if catalog else (source_root / "catalog-v001.xml")
    catalog_map = _catalog_entries(catalog_path if catalog_path.exists() else None)
    files = _source_files(root, output_path)
    if not files:
        raise ValueError(f"No supported RDF source files found under {root}")

    graph = Graph()
    origins: dict[URIRef, set[str]] = defaultdict(set)
    source_records: dict[str, SourceFile] = {}
    locations: dict[str, Path] = {}
    loaded: set[Path] = set()
    pending = list(files)
    warnings: list[dict[str, str]] = []
    imports: set[str] = set()
    while pending:
        path = pending.pop(0).resolve()
        if path in loaded or not path.is_file():
            continue
        loaded.add(path)
        rdf_format = _format(path)
        if rdf_format == "json-ld":
            _reject_remote_jsonld_context(path)
        parsed = Dataset() if rdf_format == "nquads" else Graph()
        parsed.parse(path, format=rdf_format, publicID=path.as_uri())
        for subject, predicate, obj in parsed.triples((None, None, None)):
            graph.add((subject, predicate, obj))
            if isinstance(subject, URIRef):
                origins[subject].add(_relative(path, source_root))
        source_name = _relative(path, source_root)
        source_records[source_name] = SourceFile(source_name, rdf_format, _sha256(path))
        locations[source_name] = path
        for imported in parsed.objects(None, OWL.imports):
            if not isinstance(imported, URIRef):
                continue
            import_iri = str(imported)
            imports.add(import_iri)
            imported_path = catalog_map.get(import_iri)
            if imported_path is not None:
                if imported_path.is_file() and imported_path.resolve() not in loaded:
                    pending.append(imported_path)
            elif root.is_file():
                warnings.append({"code": "IMPORT_NOT_IN_CATALOG", "iri": import_iri, "source": source_name})

    known_ontology_iris = {str(subject) for subject in graph.subjects(RDF.type, OWL.Ontology) if isinstance(subject, URIRef)}
    for imported in sorted(imports):
        if imported in known_ontology_iris:
            continue
        target = catalog_map.get(imported)
        if target is None or not target.is_file():
            warnings.append({"code": "IMPORT_UNRESOLVED_OFFLINE", "iri": imported})
    for extra in ("catalog-v001.xml", "LICENSE"):
        extra_path = source_root / extra
        if extra_path.is_file():
            locations[extra] = extra_path
    return LoadedOntology(
        graph=graph,
        origins=dict(origins),
        sources=sorted(source_records.values(), key=lambda item: item.path.casefold()),
        locations=locations,
        warnings=warnings,
        imports=sorted(imports),
    )
