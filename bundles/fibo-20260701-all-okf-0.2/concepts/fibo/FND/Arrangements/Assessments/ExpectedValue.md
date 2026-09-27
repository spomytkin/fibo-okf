---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: expected value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: theoretical value that is anticipated based on a model or hypothesis
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Expected values are often calculated using probability distributions. Note that they can be qualitative, however,
      such as certain ratings.
  disjoint_with:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/ObservedValue.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ObservedValue
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/Value.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Value
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ExpectedValue
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: expected value
type: Ontology Class
---

# expected value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ExpectedValue>

## Definition

theoretical value that is anticipated based on a model or hypothesis

## Relationships

- **Subclass of**: [Value](/concepts/fibo/FND/Arrangements/Assessments/Value.md)

## Constraints

- **Disjoint with**: [ObservedValue](/concepts/fibo/FND/Arrangements/Assessments/ObservedValue.md)

## Annotations

- **label**: expected value
- **definition**: theoretical value that is anticipated based on a model or hypothesis
- **explanatoryNote**: Expected values are often calculated using probability distributions. Note that they can be qualitative, however, such as certain ratings.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
