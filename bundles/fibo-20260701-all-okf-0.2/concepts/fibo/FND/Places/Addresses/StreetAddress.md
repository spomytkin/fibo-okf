---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: street address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: index to a location that consists of a primary address number, predirectional, street name, suffix, postdirectional,
      and an optional secondary unit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostdirectionalSymbol
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostdirectionalSymbol
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PredirectionalSymbol
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPredirectionalSymbol
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PrimaryAddressNumber
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPrimaryAddressNumber
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnit
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasSecondaryUnit
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetName
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStreetName
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetSuffix
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStreetSuffix
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/AddressComponent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressComponent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetAddress
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: street address
type: Ontology Class
---

# street address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetAddress>

## Definition

index to a location that consists of a primary address number, predirectional, street name, suffix, postdirectional, and an optional secondary unit

## Relationships

- **Subclass of**: [AddressComponent](/concepts/fibo/FND/Places/Addresses/AddressComponent.md)

## Constraints

- **[hasPostdirectionalSymbol](/concepts/fibo/FND/Places/Addresses/hasPostdirectionalSymbol.md)**: min qualified cardinality 0 of type [PostdirectionalSymbol](/concepts/fibo/FND/Places/Addresses/PostdirectionalSymbol.md)
- **[hasPredirectionalSymbol](/concepts/fibo/FND/Places/Addresses/hasPredirectionalSymbol.md)**: min qualified cardinality 0 of type [PredirectionalSymbol](/concepts/fibo/FND/Places/Addresses/PredirectionalSymbol.md)
- **[hasPrimaryAddressNumber](/concepts/fibo/FND/Places/Addresses/hasPrimaryAddressNumber.md)**: max qualified cardinality 1 of type [PrimaryAddressNumber](/concepts/fibo/FND/Places/Addresses/PrimaryAddressNumber.md)
- **[hasSecondaryUnit](/concepts/fibo/FND/Places/Addresses/hasSecondaryUnit.md)**: min qualified cardinality 0 of type [SecondaryUnit](/concepts/fibo/FND/Places/Addresses/SecondaryUnit.md)
- **[hasStreetName](/concepts/fibo/FND/Places/Addresses/hasStreetName.md)**: some values from of type [StreetName](/concepts/fibo/FND/Places/Addresses/StreetName.md)
- **[hasStreetSuffix](/concepts/fibo/FND/Places/Addresses/hasStreetSuffix.md)**: min qualified cardinality 0 of type [StreetSuffix](/concepts/fibo/FND/Places/Addresses/StreetSuffix.md)

## Annotations

- **label**: street address
- **definition**: index to a location that consists of a primary address number, predirectional, street name, suffix, postdirectional, and an optional secondary unit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
