# OWL to OKF 0.2 converter

`owl2okf` is a reproducible command-line tool for projecting local RDF/OWL ontologies into OKF 0.2 Markdown bundles. The included FIBO profile creates versioned FIBO bundles; a generic profile is also available.

Install from this directory:

```console
python -m pip install .
owl2okf compile ../ ../bundles --profile fibo
```

Compilation runs offline. Local `owl:imports` are resolved through an OASIS XML catalog, and remote JSON-LD contexts are rejected. Each bundle includes the copied source files, SHA-256 provenance, a machine-readable bundle manifest, browsable indexes, and a conversion log. The output parent must not already exist.

Use `--scope domains` to create one bundle per FIBO domain, or `--scope BE` to create one domain bundle. Use `--profile generic` for the generic OWL projection.
