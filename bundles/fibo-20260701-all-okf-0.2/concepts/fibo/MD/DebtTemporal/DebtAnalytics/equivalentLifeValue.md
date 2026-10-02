---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equivalent life value
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The Equivalent Life in years at the stated date.
  domain:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/equivalentLifeValue
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: equivalent life value
type: Ontology Property
---

# equivalent life value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/equivalentLifeValue>

## Definition

The Equivalent Life in years at the stated date.

## Relationships

- **Domain**: [EquivalentLifeAnalytic](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic.md)
- **Range**: [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)

## Annotations

- **label** (en): equivalent life value
- **definition** (en): The Equivalent Life in years at the stated date.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
