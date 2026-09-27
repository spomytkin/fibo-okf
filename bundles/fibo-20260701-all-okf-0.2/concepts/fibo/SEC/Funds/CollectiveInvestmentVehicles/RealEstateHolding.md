---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: real estate holding
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: tangible asset consisting of real estate that is owned or controlled by an individual, organization, or entity
      for investment, operational, or strategic purposes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealEstate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Portfolio
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/RealEstateHolding
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: real estate holding
type: Ontology Class
---

# real estate holding

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/RealEstateHolding>

## Definition

tangible asset consisting of real estate that is owned or controlled by an individual, organization, or entity for investment, operational, or strategic purposes

## Relationships

- **Subclass of**: [Portfolio](/concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [RealEstate](/concepts/fibo/FND/Places/RealProperty/RealEstate.md)

## Annotations

- **label** (en): real estate holding
- **definition** (en): tangible asset consisting of real estate that is owned or controlled by an individual, organization, or entity for investment, operational, or strategic purposes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
