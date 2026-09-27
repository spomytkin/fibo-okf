---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rounding convention
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The rounding convention used in the calculation method.
  domain:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/roundingConvention
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: rounding convention
type: Ontology Property
---

# rounding convention

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/roundingConvention>

## Definition

The rounding convention used in the calculation method.

## Relationships

- **Domain**: [YieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): rounding convention
- **definition** (en): The rounding convention used in the calculation method.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
