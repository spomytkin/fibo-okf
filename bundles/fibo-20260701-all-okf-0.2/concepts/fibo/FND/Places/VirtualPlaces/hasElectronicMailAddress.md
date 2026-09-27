---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has electronic mail address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies an electronic messaging endpoint at which some entity may be located or contacted or may receive correspondence
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: has e-mail address
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: has email address
  range:
  - concept: /concepts/fibo/FND/Places/VirtualPlaces/ElectronicMailAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/ElectronicMailAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Places/Addresses/hasAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/hasElectronicMailAddress
sources:
- id: fibo-source-408986d983
  resource: references/fibo/FND/Places/VirtualPlaces.rdf
  sha256: 408986d983df3f87901b90ff49e3ba3f323f94111338f7674037f481104e6007
  title: FIBO source FND/Places/VirtualPlaces.rdf
title: has electronic mail address
type: Ontology Property
---

# has electronic mail address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/hasElectronicMailAddress>

## Definition

specifies an electronic messaging endpoint at which some entity may be located or contacted or may receive correspondence

## Relationships

- **Range**: [ElectronicMailAddress](/concepts/fibo/FND/Places/VirtualPlaces/ElectronicMailAddress.md)
- **Subproperty of**: [hasAddress](/concepts/fibo/FND/Places/Addresses/hasAddress.md)

## Annotations

- **label**: has electronic mail address
- **definition**: specifies an electronic messaging endpoint at which some entity may be located or contacted or may receive correspondence
- **abbreviation**: has e-mail address
- **abbreviation**: has email address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
