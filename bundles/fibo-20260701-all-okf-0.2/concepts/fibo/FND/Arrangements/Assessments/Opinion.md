---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: opinion
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: judgement, appraisal, or view about something
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentEvent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/isOutputFrom
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isGeneratedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Opinion
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: opinion
type: Ontology Class
---

# opinion

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Opinion>

## Definition

judgement, appraisal, or view about something

## Constraints

- **[isOutputFrom](/concepts/fibo/FND/DatesAndTimes/Occurrences/isOutputFrom.md)**: some values from of type [AssessmentEvent](/concepts/fibo/FND/Arrangements/Assessments/AssessmentEvent.md)
- **[isGeneratedBy](/concepts/fibo/FND/Relations/Relations/isGeneratedBy.md)**: some values from of type [AgentRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole>)

## Annotations

- **label**: opinion
- **definition**: judgement, appraisal, or view about something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
