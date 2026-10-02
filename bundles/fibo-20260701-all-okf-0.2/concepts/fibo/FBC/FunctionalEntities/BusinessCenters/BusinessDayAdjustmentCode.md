---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business day adjustment code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: code used to denote a convention for specifying what happens when a date falls on a day that is weekend or holiday
      in some municipality or business center
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.fpml.org/coding-scheme/business-center
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/BusinessDayAdjustmentCode
sources:
- id: fibo-source-9bbbd18083
  resource: references/fibo/FBC/FunctionalEntities/BusinessCenters.rdf
  sha256: 9bbbd18083fbf3183af8c86eb613aa661a0110b3c02acb42c40459b17aaefe20
  title: FIBO source FBC/FunctionalEntities/BusinessCenters.rdf
title: business day adjustment code
type: Ontology Class
---

# business day adjustment code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/BusinessDayAdjustmentCode>

## Definition

code used to denote a convention for specifying what happens when a date falls on a day that is weekend or holiday in some municipality or business center

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [BusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md)

## Annotations

- **label**: business day adjustment code
- **definition**: code used to denote a convention for specifying what happens when a date falls on a day that is weekend or holiday in some municipality or business center
- **adaptedFrom**: http://www.fpml.org/coding-scheme/business-center

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
