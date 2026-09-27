---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has transliterated address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a transliterated (i.e., in Latin or Romanized ASCII) address for the registered entity
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/Address.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Address
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Places/Addresses/hasAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasTransliteratedAddress
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has transliterated address
type: Ontology Property
---

# has transliterated address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasTransliteratedAddress>

## Definition

identifies a transliterated (i.e., in Latin or Romanized ASCII) address for the registered entity

## Relationships

- **Range**: [Address](/concepts/fibo/FND/Places/Addresses/Address.md)
- **Subproperty of**: [hasAddress](/concepts/fibo/FND/Places/Addresses/hasAddress.md)

## Annotations

- **label**: has transliterated address
- **definition**: identifies a transliterated (i.e., in Latin or Romanized ASCII) address for the registered entity
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
