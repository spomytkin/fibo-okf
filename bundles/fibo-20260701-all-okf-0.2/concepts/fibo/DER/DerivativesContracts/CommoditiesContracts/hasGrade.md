---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has grade
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The grade of oil e.g. Brent Crude.
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/OilCommodity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/OilCommodity
  range:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/OilGrade.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/OilGrade
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/hasGrade
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: has grade
type: Ontology Property
---

# has grade

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/hasGrade>

## Definition

The grade of oil e.g. Brent Crude.

## Relationships

- **Domain**: [OilCommodity](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/OilCommodity.md)
- **Range**: [OilGrade](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/OilGrade.md)

## Annotations

- **label** (en): has grade
- **definition** (en): The grade of oil e.g. Brent Crude.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
