---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: housing unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: house, an apartment, a mobile home or trailer, a group of rooms, or a single room occupied as separate living quarters,
      or if vacant, intended for occupancy as separate living quarters
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Separate living quarters are those in which the occupants live separately from any other individuals in the building
      and which have direct access from outside the building or through a common hall. For vacant units, the criteria of separateness
      and direct access are applied to the intended occupants whenever possible.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/PhysicalLocation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/HousingUnit
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: housing unit
type: Ontology Class
---

# housing unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/HousingUnit>

## Definition

house, an apartment, a mobile home or trailer, a group of rooms, or a single room occupied as separate living quarters, or if vacant, intended for occupancy as separate living quarters

## Relationships

- **Subclass of**: [PhysicalLocation](<https://www.omg.org/spec/Commons/Locations/PhysicalLocation>)

## Constraints

- **[hasAddress](/concepts/fibo/FND/Places/Addresses/hasAddress.md)**: all values from of type [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)

## Annotations

- **label**: housing unit
- **definition**: house, an apartment, a mobile home or trailer, a group of rooms, or a single room occupied as separate living quarters, or if vacant, intended for occupancy as separate living quarters
- **explanatoryNote**: Separate living quarters are those in which the occupants live separately from any other individuals in the building and which have direct access from outside the building or through a common hall. For vacant units, the criteria of separateness and direct access are applied to the intended occupants whenever possible.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
