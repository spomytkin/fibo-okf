---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: delivery address code set
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system of numeric codes that substitute for specified delivery point details according to the U.S. Postal Service
      Publication 28
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/USPostalServiceAddressIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DeliveryAddressCodeSet
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: delivery address code set
type: Ontology Class
---

# delivery address code set

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DeliveryAddressCodeSet>

## Definition

system of numeric codes that substitute for specified delivery point details according to the U.S. Postal Service Publication 28

## Relationships

- **See also**: [pub28.pdf](<https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf>)
- **Subclass of**: [CodeSet](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet>)
- **Subclass of**: [IdentificationScheme](<https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [USPostalServiceAddressIdentifier](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/USPostalServiceAddressIdentifier.md)

## Annotations

- **label**: delivery address code set
- **definition**: system of numeric codes that substitute for specified delivery point details according to the U.S. Postal Service Publication 28

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
