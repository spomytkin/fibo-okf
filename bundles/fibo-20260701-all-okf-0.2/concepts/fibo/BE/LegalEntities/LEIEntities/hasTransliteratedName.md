---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has transliterated name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a transliterated (i.e., in Latin or Romanized ASCII) representation of a name for the entity
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Designators/hasTextualName
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasTransliteratedName
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: has transliterated name
type: Ontology Property
---

# has transliterated name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasTransliteratedName>

## Definition

a transliterated (i.e., in Latin or Romanized ASCII) representation of a name for the entity

## Relationships

- **Subproperty of**: [hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)

## Annotations

- **label**: has transliterated name
- **definition**: a transliterated (i.e., in Latin or Romanized ASCII) representation of a name for the entity
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
