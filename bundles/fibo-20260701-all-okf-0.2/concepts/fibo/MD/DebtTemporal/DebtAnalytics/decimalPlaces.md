---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: decimal places
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The number of decimal places used in the publication of the factor value.
  domain:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/PoolFactor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolFactor
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/decimalPlaces
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: decimal places
type: Ontology Property
---

# decimal places

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/decimalPlaces>

## Definition

The number of decimal places used in the publication of the factor value.

## Relationships

- **Domain**: [PoolFactor](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/PoolFactor.md)
- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label** (en): decimal places
- **definition** (en): The number of decimal places used in the publication of the factor value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
