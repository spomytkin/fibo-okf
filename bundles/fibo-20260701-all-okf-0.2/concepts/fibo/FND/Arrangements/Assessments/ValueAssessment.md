---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: value assessment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: assessment event to estimate the value of something
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that an appraiser in this context may be a licensed appraiser, such as a real estate appraiser or auction
      house, or a calculation agent, depending on the circumstances.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValuationMethod
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/appliesMethodology
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasAppraiser
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOutput
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValueAssessment
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: value assessment
type: Ontology Class
---

# value assessment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValueAssessment>

## Definition

assessment event to estimate the value of something

## Relationships

- **Subclass of**: [AssessmentEvent](/concepts/fibo/FND/Arrangements/Assessments/AssessmentEvent.md)

## Constraints

- **[appliesMethodology](/concepts/fibo/FND/Arrangements/Assessments/appliesMethodology.md)**: min qualified cardinality 0 of type [ValuationMethod](/concepts/fibo/FND/Arrangements/Assessments/ValuationMethod.md)
- **[hasAppraiser](/concepts/fibo/FND/Arrangements/Assessments/hasAppraiser.md)**: some values from of type [AgentRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole>)
- **[hasOutput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOutput.md)**: min qualified cardinality 0 of type [Appraisal](/concepts/fibo/FND/Arrangements/Assessments/Appraisal.md)

## Annotations

- **label**: value assessment
- **definition**: assessment event to estimate the value of something
- **explanatoryNote**: Note that an appraiser in this context may be a licensed appraiser, such as a real estate appraiser or auction house, or a calculation agent, depending on the circumstances.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
