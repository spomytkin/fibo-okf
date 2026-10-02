"""Small OKF 0.2 conformance check and separate link-quality warnings."""

from __future__ import annotations

import re
import posixpath
from dataclasses import dataclass, field
from pathlib import Path

import yaml

LINK_RE = re.compile(r"\[[^\]]*\]\((<?[^)\s]+>?)\)")
LOG_DATE_RE = re.compile(r"^## \d{4}-\d{2}-\d{2}$", re.MULTILINE)


@dataclass
class ValidationResult:
    conformance_errors: list[dict[str, str]] = field(default_factory=list)
    quality_warnings: list[dict[str, str]] = field(default_factory=list)


def _frontmatter(path: Path) -> tuple[dict | None, str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "missing frontmatter delimiter"
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, "missing closing frontmatter delimiter"
    try:
        value = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        return None, f"invalid YAML frontmatter: {exc}"
    if value is None:
        value = {}
    if not isinstance(value, dict):
        return None, "frontmatter must be a YAML mapping"
    return value, None


def validate_bundle(bundle: str | Path) -> ValidationResult:
    root = Path(bundle)
    result = ValidationResult()
    all_paths = list(root.rglob("*"))
    available_files = {
        path.relative_to(root).as_posix()
        for path in all_paths
        if path.is_file()
    }
    available_directories = {
        path.relative_to(root).as_posix()
        for path in all_paths
        if path.is_dir()
    }
    markdown = sorted((root / item for item in available_files if item.lower().endswith(".md")), key=lambda item: item.as_posix().casefold())
    for path in markdown:
        relative = path.relative_to(root).as_posix()
        name = path.name.lower()
        if name == "log.md":
            text = path.read_text(encoding="utf-8")
            if not LOG_DATE_RE.search(text):
                result.conformance_errors.append({"path": relative, "message": "log.md must contain an ISO date heading"})
            continue
        frontmatter, error = _frontmatter(path)
        if name == "index.md":
            if error:
                # Nested indexes have no frontmatter by design.
                if text_starts_frontmatter(path):
                    result.conformance_errors.append({"path": relative, "message": error})
            elif path == root / "index.md":
                if frontmatter.get("okf_version") != "0.2":
                    result.conformance_errors.append({"path": relative, "message": "root index.md must declare okf_version: '0.2'"})
                if set(frontmatter) - {"okf_version"}:
                    result.conformance_errors.append({"path": relative, "message": "root index.md may declare only okf_version"})
        else:
            if error:
                result.conformance_errors.append({"path": relative, "message": error})
            elif not isinstance(frontmatter.get("type"), str) or not frontmatter["type"].strip():
                result.conformance_errors.append({"path": relative, "message": "concept frontmatter needs a non-empty type"})

        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            href = match.group(1).strip("<>")
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                resolved = posixpath.normpath(target.lstrip("/"))
            else:
                resolved = posixpath.normpath(posixpath.join(Path(relative).parent.as_posix(), target))
            if resolved in available_directories:
                resolved = posixpath.join(resolved, "index.md")
            if resolved not in available_files:
                result.quality_warnings.append({"path": relative, "message": f"broken local link: {href}"})
    return result


def validate_projection(projection, bundle: str | Path) -> ValidationResult:
    """Validate projected documents in memory and check generated bundle headers.

    This avoids rereading tens of thousands of Markdown files on synced or
    network-backed filesystems while still checking every projected document.
    """
    root = Path(bundle)
    result = ValidationResult()
    expected_paths = set(projection.documents)
    expected_paths.add("index.md")
    expected_paths.add("log.md")
    directories = set()
    for relative in projection.documents:
        directory = Path(relative).parent
        while str(directory) != ".":
            directories.add(directory.as_posix())
            directory = directory.parent
    expected_paths.update(f"{directory}/index.md" for directory in directories)

    for relative, document in projection.documents.items():
        frontmatter = document.frontmatter
        if not isinstance(frontmatter.get("type"), str) or not frontmatter["type"].strip():
            result.conformance_errors.append({"path": relative, "message": "concept frontmatter needs a non-empty type"})
        try:
            serialized = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=True)
            if not isinstance(yaml.safe_load(serialized), dict):
                raise yaml.YAMLError("frontmatter is not a mapping after YAML round-trip")
        except yaml.YAMLError as exc:
            result.conformance_errors.append({"path": relative, "message": f"invalid YAML frontmatter: {exc}"})

        for match in LINK_RE.finditer(document.body):
            href = match.group(1).strip("<>")
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                resolved = posixpath.normpath(target.lstrip("/"))
            else:
                resolved = posixpath.normpath(posixpath.join(Path(relative).parent.as_posix(), target))
            if resolved in directories:
                resolved = posixpath.join(resolved, "index.md")
            if resolved not in expected_paths:
                result.quality_warnings.append({"path": relative, "message": f"broken local link: {href}"})

    index = root / "index.md"
    if not index.is_file():
        result.conformance_errors.append({"path": "index.md", "message": "bundle root index.md is missing"})
    else:
        frontmatter, error = _frontmatter(index)
        if error:
            result.conformance_errors.append({"path": "index.md", "message": error})
        elif frontmatter.get("okf_version") != "0.2":
            result.conformance_errors.append({"path": "index.md", "message": "root index.md must declare okf_version: '0.2'"})
        elif set(frontmatter) - {"okf_version"}:
            result.conformance_errors.append({"path": "index.md", "message": "root index.md may declare only okf_version"})
    log = root / "log.md"
    if not log.is_file() or not LOG_DATE_RE.search(log.read_text(encoding="utf-8")):
        result.conformance_errors.append({"path": "log.md", "message": "log.md must contain an ISO date heading"})
    for relative in directories:
        if not (root / relative / "index.md").is_file():
            result.conformance_errors.append({"path": f"{relative}/index.md", "message": "nested index.md is missing"})
    return result


def text_starts_frontmatter(path: Path) -> bool:
    return path.read_text(encoding="utf-8").startswith("---\n")
