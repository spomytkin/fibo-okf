---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: assessment event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event involving the evaluation or estimation of the nature, quality, or ability of someone or something
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentReport
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOutput
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Opinion
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOutput
  - cardinality: 0
    kind: min_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentActivity
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentEvent
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: assessment event
type: Ontology Class
---

# assessment event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentEvent>

## Definition

event involving the evaluation or estimation of the nature, quality, or ability of someone or something

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Constraints

- **[hasOutput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOutput.md)**: min qualified cardinality 0 of type [AssessmentReport](/concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md)
- **[hasOutput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOutput.md)**: some values from of type [Opinion](/concepts/fibo/FND/Arrangements/Assessments/Opinion.md)
- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: min cardinality 0
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [AssessmentActivity](/concepts/fibo/FND/Arrangements/Assessments/AssessmentActivity.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [AgentRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole>)

## Annotations

- **label**: assessment event
- **definition**: event involving the evaluation or estimation of the nature, quality, or ability of someone or something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
