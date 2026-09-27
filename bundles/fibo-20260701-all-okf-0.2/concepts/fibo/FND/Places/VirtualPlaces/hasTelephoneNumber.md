---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has telephone number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a virtual address composed of a sequence of digits and symbols that may be assigned to a fixed-line telephone
      subscriber station, a wireless electronic telephony device, such as a radio telephone or a mobile telephone, or other
      similar device or service
  range:
  - concept: /concepts/fibo/FND/Places/VirtualPlaces/TelephoneNumber.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/TelephoneNumber
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Places/Addresses/hasAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/hasTelephoneNumber
sources:
- id: fibo-source-408986d983
  resource: references/fibo/FND/Places/VirtualPlaces.rdf
  sha256: 408986d983df3f87901b90ff49e3ba3f323f94111338f7674037f481104e6007
  title: FIBO source FND/Places/VirtualPlaces.rdf
title: has telephone number
type: Ontology Property
---

# has telephone number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/hasTelephoneNumber>

## Definition

indicates a virtual address composed of a sequence of digits and symbols that may be assigned to a fixed-line telephone subscriber station, a wireless electronic telephony device, such as a radio telephone or a mobile telephone, or other similar device or service

## Relationships

- **Range**: [TelephoneNumber](/concepts/fibo/FND/Places/VirtualPlaces/TelephoneNumber.md)
- **Subproperty of**: [hasAddress](/concepts/fibo/FND/Places/Addresses/hasAddress.md)

## Annotations

- **label**: has telephone number
- **definition**: indicates a virtual address composed of a sequence of digits and symbols that may be assigned to a fixed-line telephone subscriber station, a wireless electronic telephony device, such as a radio telephone or a mobile telephone, or other similar device or service

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
