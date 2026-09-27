---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: electronic mail address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: virtual address that defines an electronic messaging endpoint to which email messages can be delivered, typically
      via an Simple Mail Transfer Protocol (SMTP) based communications system
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: e-mail address
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: email address
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Electronic mail, abbreviated e-mail or email, is a method of composing, sending, and receiving messages over electronic
      communication systems. The term e-mail applies both to the Internet e-mail system based on the Simple Mail Transfer
      Protocol (SMTP) and to intranet systems allowing users within one company or organization to send messages to each other.
      Often these workgroup collaboration systems natively use non-standard protocols but have some form of gateway to allow
      them to send and receive Internet e-mail. Some organizations may use the Internet protocols for internal e-mail service.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/VirtualAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/VirtualAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/ElectronicMailAddress
sources:
- id: fibo-source-408986d983
  resource: references/fibo/FND/Places/VirtualPlaces.rdf
  sha256: 408986d983df3f87901b90ff49e3ba3f323f94111338f7674037f481104e6007
  title: FIBO source FND/Places/VirtualPlaces.rdf
title: electronic mail address
type: Ontology Class
---

# electronic mail address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/ElectronicMailAddress>

## Definition

virtual address that defines an electronic messaging endpoint to which email messages can be delivered, typically via an Simple Mail Transfer Protocol (SMTP) based communications system

## Relationships

- **Subclass of**: [VirtualAddress](/concepts/fibo/FND/Places/Addresses/VirtualAddress.md)

## Annotations

- **label**: electronic mail address
- **definition**: virtual address that defines an electronic messaging endpoint to which email messages can be delivered, typically via an Simple Mail Transfer Protocol (SMTP) based communications system
- **abbreviation**: e-mail address
- **abbreviation**: email address
- **explanatoryNote**: Electronic mail, abbreviated e-mail or email, is a method of composing, sending, and receiving messages over electronic communication systems. The term e-mail applies both to the Internet e-mail system based on the Simple Mail Transfer Protocol (SMTP) and to intranet systems allowing users within one company or organization to send messages to each other. Often these workgroup collaboration systems natively use non-standard protocols but have some form of gateway to allow them to send and receive Internet e-mail. Some organizations may use the Internet protocols for internal e-mail service.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
