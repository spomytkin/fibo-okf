---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: oil commodity
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: generated resource that is a viscous liquid derived from petroleum, including for use as fuel, or as a lubricant,
      and the manufacture of many types of paints, plastics, and other materials
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/OilGrade
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/hasGrade
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/GeneratedResource.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/GeneratedResource
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/OilCommodity
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: oil commodity
type: Ontology Class
---

# oil commodity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/OilCommodity>

## Definition

generated resource that is a viscous liquid derived from petroleum, including for use as fuel, or as a lubricant, and the manufacture of many types of paints, plastics, and other materials

## Relationships

- **Subclass of**: [GeneratedResource](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/GeneratedResource.md)

## Constraints

- **[hasGrade](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/hasGrade.md)**: some values from of type [OilGrade](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/OilGrade.md)

## Annotations

- **label** (en): oil commodity
- **definition** (en): generated resource that is a viscous liquid derived from petroleum, including for use as fuel, or as a lubricant, and the manufacture of many types of paints, plastics, and other materials

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
