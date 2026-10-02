"""Command line entry point for the generic OWL-to-OKF compiler."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .compiler import compile_ontology


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="owl2okf",
        description="Compile local RDF/OWL sources into reproducible OKF 0.2 bundles.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    compile_parser = subparsers.add_parser("compile", help="parse, model, project, render, and report")
    compile_parser.add_argument("source", type=Path, help="RDF file or directory of RDF/OWL sources")
    compile_parser.add_argument("output", type=Path, help="new output directory for versioned bundle(s) and report")
    compile_parser.add_argument("--profile", default="fibo", choices=("fibo", "generic"), help="ontology projection profile")
    compile_parser.add_argument("--scope", default="all", help="all, domains (FIBO only), or one FIBO domain code such as BE")
    compile_parser.add_argument("--catalog", type=Path, help="OASIS XML catalog; defaults to catalog-v001.xml beside the source")
    compile_parser.add_argument("--fibo-version", help="override version inferred from owl:versionIRI")
    parser.add_argument("--version", action="version", version=f"owl2okf {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "compile":
        try:
            report = compile_ontology(
                args.source,
                args.output,
                profile_name=args.profile,
                scope=args.scope,
                catalog=args.catalog,
                fibo_version=args.fibo_version,
            )
        except Exception as exc:
            print(f"owl2okf: error: {exc}", file=sys.stderr)
            return 2
        for bundle in report["bundles"]:
            print(args.output / bundle["path"])
        print(args.output / "conversion-report.json")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
