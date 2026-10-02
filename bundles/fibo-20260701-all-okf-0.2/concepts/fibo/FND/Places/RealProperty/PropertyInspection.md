---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: property inspection
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event that involves analyzing one or more aspects of a real property
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The concept of a property inspection is separate from conducting an overarching appraisal. Examples are termite
      inspections, construction inspections, evaluation for completion of some milestone, improvement, correction, etc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PropertyInspectionReport
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOutput
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PropertyInspection
sources:
- id: fibo-source-f0e5ecd06c
  resource: references/fibo/FND/Places/RealProperty.rdf
  sha256: f0e5ecd06c164d1e5fff0c1236869b2014bcba3d7008365dcc2c7363064202bd
  title: FIBO source FND/Places/RealProperty.rdf
title: property inspection
type: Ontology Class
---

# property inspection

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PropertyInspection>

## Definition

event that involves analyzing one or more aspects of a real property

## Relationships

- **Subclass of**: [AssessmentEvent](/concepts/fibo/FND/Arrangements/Assessments/AssessmentEvent.md)

## Constraints

- **[hasOutput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOutput.md)**: min qualified cardinality 0 of type [PropertyInspectionReport](/concepts/fibo/FND/Places/RealProperty/PropertyInspectionReport.md)
- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: some values from of type [RealProperty](/concepts/fibo/FND/Places/RealProperty/RealProperty.md)

## Annotations

- **label**: property inspection
- **definition**: event that involves analyzing one or more aspects of a real property
- **explanatoryNote**: The concept of a property inspection is separate from conducting an overarching appraisal. Examples are termite inspections, construction inspections, evaluation for completion of some milestone, improvement, correction, etc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
