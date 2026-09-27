---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: general delivery address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: delivery address that uses the words 'GENERAL DELIVERY', uppercase preferred, spelled out (no abbreviation), in
      place of a street address
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The value of the +4 component of a ZIP+4 code should be '9999'.
  disjoint_with:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: GENERAL DELIVERY
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/GeneralDeliveryAddress
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: general delivery address
type: Ontology Class
---

# general delivery address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/GeneralDeliveryAddress>

## Definition

delivery address that uses the words 'GENERAL DELIVERY', uppercase preferred, spelled out (no abbreviation), in place of a street address

## Relationships

- **Subclass of**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)

## Constraints

- **Disjoint with**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **[hasAddressLine1](/concepts/fibo/FND/Places/Addresses/hasAddressLine1.md)**: has value value `GENERAL DELIVERY`

## Annotations

- **label**: general delivery address
- **definition**: delivery address that uses the words 'GENERAL DELIVERY', uppercase preferred, spelled out (no abbreviation), in place of a street address
- **explanatoryNote**: The value of the +4 component of a ZIP+4 code should be '9999'.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
