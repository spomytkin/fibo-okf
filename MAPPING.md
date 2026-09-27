# OWL to OKF mapping

This repository uses OKF 0.2 as a readable projection of RDF/OWL. The source ontology remains authoritative. The `owl` frontmatter key is a producer-defined extension for structured OWL semantics; it is not part of the OKF base schema.

## Identity and source provenance

- Every projected entity keeps its canonical ontology IRI in OKF's `resource` field.
- Its bundle-relative Markdown path is a stable document identifier, generated from the IRI through the selected profile.
- `sources` identifies each ontology file that asserted statements about the entity. Entries include a bundle-relative source path and a `sha256` extension for content identity.
- Generated concepts are not marked `verified`. A conversion run does not independently verify the truth of the source ontology.
- Conversion is asserted-only. No RDFS or OWL inference is added to the output.

## `owl` extension

Relationship values are stored under keys such as `subclass_of`, `equivalent_to`, `disjoint_with`, `domain`, `range`, `inverse_of`, and `subproperty_of`. Each target records its canonical `resource`; when it is included in the current bundle, the target also has a bundle-absolute `concept` path. The Markdown body gives each link its relationship meaning in prose, as OKF itself defines links as untyped.

Basic restrictions use `owl.restrictions` entries with `property`, `kind`, and the available `cardinality`, `filler`, or `value` fields. Property characteristics, RDF types, deprecation, and literal annotations are represented in `owl` as well. Complex expressions that are not projected are listed in `conversion-report.json`; the bundled source files retain their full RDF representation.

## Profiles

The generic profile projects explicitly typed ontology entities without imposing FIBO-specific paths or annotation choices. The FIBO profile is configured in `converter/src/owl2okf/profiles/fibo/profile.yaml`; it prioritizes SKOS preferred labels, then RDFS labels, and mirrors the FIBO ontology-module hierarchy under `concepts/fibo/`.

The output `index.md` files are generated navigation aids. The bundle root declares `okf_version: "0.2"`; nested indexes and `log.md` use the format's reserved-file conventions.
