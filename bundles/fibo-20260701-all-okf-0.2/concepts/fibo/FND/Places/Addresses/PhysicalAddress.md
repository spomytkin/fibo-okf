---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: physical address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical address where communications can be addressed, papers served or representatives located for any kind of
      organization or person
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: An address may be used as an index to the location of a building, apartment, office within an office block, or
      other structure or parcel of land, often using political boundaries and street names as references, along with other
      information such as house or building numbers or names. Some addresses also contain secondary elements such as apartment
      or building numbers, or special codes to aid routing of mail and packages.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Typically, addresses will have only one postcode expressed either as a string value or individual, and only a municipality
      (individual) or city (string value).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Locations/PhysicalLocation
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/isIndexTo
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Postcode
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasIndividualPostcode
  - cardinality: 1
    filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
  - cardinality: 1
    filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasCityName
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Locations/Country
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasCountry
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Locations/Municipality
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasMunicipality
  - filler: https://www.omg.org/spec/Commons/Locations/CountrySubdivision
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Locations/hasSubdivision
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/Address.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Address
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: physical address
type: Ontology Class
---

# physical address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress>

## Definition

physical address where communications can be addressed, papers served or representatives located for any kind of organization or person

## Relationships

- **Subclass of**: [Address](/concepts/fibo/FND/Places/Addresses/Address.md)

## Constraints

- **[isIndexTo](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices/isIndexTo.md)**: min qualified cardinality 0 of type [PhysicalLocation](<https://www.omg.org/spec/Commons/Locations/PhysicalLocation>)
- **[hasIndividualPostcode](/concepts/fibo/FND/Places/Addresses/hasIndividualPostcode.md)**: max qualified cardinality 1 of type [Postcode](/concepts/fibo/FND/Places/Addresses/Postcode.md)
- **[hasPostalCode](/concepts/fibo/FND/Places/Addresses/hasPostalCode.md)**: max qualified cardinality 1 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[hasCityName](<https://www.omg.org/spec/Commons/Locations/hasCityName>)**: max qualified cardinality 1 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[hasCountry](<https://www.omg.org/spec/Commons/Locations/hasCountry>)**: max qualified cardinality 1 of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[hasMunicipality](<https://www.omg.org/spec/Commons/Locations/hasMunicipality>)**: max qualified cardinality 1 of type [Municipality](<https://www.omg.org/spec/Commons/Locations/Municipality>)
- **[hasSubdivision](<https://www.omg.org/spec/Commons/Locations/hasSubdivision>)**: some values from of type [CountrySubdivision](<https://www.omg.org/spec/Commons/Locations/CountrySubdivision>)

## Annotations

- **label** (en): physical address
- **definition**: physical address where communications can be addressed, papers served or representatives located for any kind of organization or person
- **scopeNote**: An address may be used as an index to the location of a building, apartment, office within an office block, or other structure or parcel of land, often using political boundaries and street names as references, along with other information such as house or building numbers or names. Some addresses also contain secondary elements such as apartment or building numbers, or special codes to aid routing of mail and packages.
- **usageNote**: Typically, addresses will have only one postcode expressed either as a string value or individual, and only a municipality (individual) or city (string value).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
