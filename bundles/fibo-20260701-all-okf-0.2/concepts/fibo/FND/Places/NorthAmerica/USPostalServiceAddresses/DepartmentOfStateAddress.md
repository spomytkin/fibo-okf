---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Department of State address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: delivery address whose delivery address line uses 'UNIT' followed by the unit identifier, followed by 'BOX' followed
      by box number, in place of a street address, 'DPO' as the literal value for the city, and the appropriate armed forces
      subdivision code in place of a subdivision (state) code
  disjoint_with:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DepartmentOfStateUnitComponent
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/Mailbox
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Locations/hasCityName
    value: DPO
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DepartmentOfStateAddress
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: Department of State address
type: Ontology Class
---

# Department of State address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DepartmentOfStateAddress>

## Definition

delivery address whose delivery address line uses 'UNIT' followed by the unit identifier, followed by 'BOX' followed by box number, in place of a street address, 'DPO' as the literal value for the city, and the appropriate armed forces subdivision code in place of a subdivision (state) code

## Relationships

- **Subclass of**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)

## Constraints

- **Disjoint with**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [DepartmentOfStateUnitComponent](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/DepartmentOfStateUnitComponent.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [Mailbox](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/Mailbox.md)
- **[hasCityName](<https://www.omg.org/spec/Commons/Locations/hasCityName>)**: has value value `DPO`

## Annotations

- **label**: Department of State address
- **definition**: delivery address whose delivery address line uses 'UNIT' followed by the unit identifier, followed by 'BOX' followed by box number, in place of a street address, 'DPO' as the literal value for the city, and the appropriate armed forces subdivision code in place of a subdivision (state) code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
