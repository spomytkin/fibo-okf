---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: qualitative value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: value that has less precision or accuracy than a value determined via quantitative methods and which is usually
      expressed in codes rather than actual numbers
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO/IEC 5207:2024(en), Information technology - Data usage - Terminology and use cases
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Qualitative values may follow nominal or ordinal scales, and may be expressed as enumerations.
  disjoint_with:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/QuantitativeValue.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/QuantitativeValue
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/Value.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Value
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/QualitativeValue
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: qualitative value
type: Ontology Class
---

# qualitative value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/QualitativeValue>

## Definition

value that has less precision or accuracy than a value determined via quantitative methods and which is usually expressed in codes rather than actual numbers

## Relationships

- **Subclass of**: [Value](/concepts/fibo/FND/Arrangements/Assessments/Value.md)

## Constraints

- **Disjoint with**: [QuantitativeValue](/concepts/fibo/FND/Arrangements/Assessments/QuantitativeValue.md)

## Annotations

- **label**: qualitative value
- **definition**: value that has less precision or accuracy than a value determined via quantitative methods and which is usually expressed in codes rather than actual numbers
- **adaptedFrom**: ISO/IEC 5207:2024(en), Information technology - Data usage - Terminology and use cases
- **explanatoryNote**: Qualitative values may follow nominal or ordinal scales, and may be expressed as enumerations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
