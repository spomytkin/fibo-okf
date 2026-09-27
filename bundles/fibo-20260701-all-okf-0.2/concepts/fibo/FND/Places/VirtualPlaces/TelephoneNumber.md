---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: telephone number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: virtual address that may be assigned to a fixed-line telephone subscriber station connected to a telephone line
      or to a wireless electronic telephony device, such as a radio telephone or a mobile telephone, or to other devices or
      services for data transmission via the public switched telephone network (PSTN) or other public and private networks
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: phone number
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Telephone numbers are assigned within the framework of a national or regional telephone numbering plan to subscribers
      by telephone service operators, which may be commercial entities, state-controlled administrations, or other telecommunication
      industry associations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/VirtualAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/VirtualAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/TelephoneNumber
sources:
- id: fibo-source-408986d983
  resource: references/fibo/FND/Places/VirtualPlaces.rdf
  sha256: 408986d983df3f87901b90ff49e3ba3f323f94111338f7674037f481104e6007
  title: FIBO source FND/Places/VirtualPlaces.rdf
title: telephone number
type: Ontology Class
---

# telephone number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/TelephoneNumber>

## Definition

virtual address that may be assigned to a fixed-line telephone subscriber station connected to a telephone line or to a wireless electronic telephony device, such as a radio telephone or a mobile telephone, or to other devices or services for data transmission via the public switched telephone network (PSTN) or other public and private networks

## Relationships

- **Subclass of**: [VirtualAddress](/concepts/fibo/FND/Places/Addresses/VirtualAddress.md)

## Annotations

- **label**: telephone number
- **definition**: virtual address that may be assigned to a fixed-line telephone subscriber station connected to a telephone line or to a wireless electronic telephony device, such as a radio telephone or a mobile telephone, or to other devices or services for data transmission via the public switched telephone network (PSTN) or other public and private networks
- **abbreviation**: phone number
- **explanatoryNote**: Telephone numbers are assigned within the framework of a national or regional telephone numbering plan to subscribers by telephone service operators, which may be commercial entities, state-controlled administrations, or other telecommunication industry associations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
