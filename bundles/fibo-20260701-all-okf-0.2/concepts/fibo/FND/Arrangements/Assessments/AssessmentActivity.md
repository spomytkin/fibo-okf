---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: assessment activity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: activity involving the evaluation or estimation of the nature, quality, ability, or value of someone or something
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentActivity
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: assessment activity
type: Ontology Class
---

# assessment activity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentActivity>

## Definition

activity involving the evaluation or estimation of the nature, quality, ability, or value of someone or something

## Relationships

- **Subclass of**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Constraints

- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: min cardinality 0
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [AgentRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole>)

## Annotations

- **label**: assessment activity
- **definition**: activity involving the evaluation or estimation of the nature, quality, ability, or value of someone or something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
