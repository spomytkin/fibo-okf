---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: next put
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The next available put date for the issue, as at the current time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/PutEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutEvent
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NextPut
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: next put
type: Ontology Class
---

# next put

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NextPut>

## Definition

The next available put date for the issue, as at the current time.

## Relationships

- **Subclass of**: [PutEvent](/concepts/fibo/SEC/Debt/DebtInstruments/PutEvent.md)

## Annotations

- **label** (en): next put
- **definition** (en): The next available put date for the issue, as at the current time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
