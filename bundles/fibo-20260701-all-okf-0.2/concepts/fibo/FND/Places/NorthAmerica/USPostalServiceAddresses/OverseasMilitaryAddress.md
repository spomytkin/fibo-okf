---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: overseas military address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: delivery address whose delivery address line uses an abbreviation for the unit or command such as 'CMR', 'PSC',
      or 'UNIT', or 'HC', followed by the unit identifier, followed by 'BOX' followed by box number, in place of a street
      address, either 'APO' or 'FPO' as the literal value for the city and the appropriate armed forces subdivision code in
      place of a subdivision (state) code
  disjoint_with:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Locations/hasCityName
    value: N5ec1027f8d394c91b524ff10084f470f
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/OverseasMilitaryAddress
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: overseas military address
type: Ontology Class
---

# overseas military address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/OverseasMilitaryAddress>

## Definition

delivery address whose delivery address line uses an abbreviation for the unit or command such as 'CMR', 'PSC', or 'UNIT', or 'HC', followed by the unit identifier, followed by 'BOX' followed by box number, in place of a street address, either 'APO' or 'FPO' as the literal value for the city and the appropriate armed forces subdivision code in place of a subdivision (state) code

## Relationships

- **Subclass of**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)

## Constraints

- **Disjoint with**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **[hasAddressLine1](/concepts/fibo/FND/Places/Addresses/hasAddressLine1.md)**: some values from of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[hasCityName](<https://www.omg.org/spec/Commons/Locations/hasCityName>)**: some values from value `N5ec1027f8d394c91b524ff10084f470f`

## Annotations

- **label**: overseas military address
- **definition**: delivery address whose delivery address line uses an abbreviation for the unit or command such as 'CMR', 'PSC', or 'UNIT', or 'HC', followed by the unit identifier, followed by 'BOX' followed by box number, in place of a street address, either 'APO' or 'FPO' as the literal value for the city and the appropriate armed forces subdivision code in place of a subdivision (state) code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
