---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: environmental project
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specific initiative, activity, or investment aimed at improving environmental sustainability, reducing ecological
      harm, or addressing environmental challenges
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Key characteristics of an environmental or sustainability project include achieving measurable positive environmental
      outcomes, and aligning with broader sustainability goals, such as those outlined in international frameworks (e.g.,
      the United Nations Sustainable Development Goals (SDGs), Paris Agreement).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such projects are designed to align with environmental goals, such as mitigating climate change, conserving natural
      resources, protecting biodiversity, and promoting a circular economy.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MilestoneSchedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/AssessmentBoundary
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/hasAssessmentBoundary
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/EnvironmentalProgram
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Project.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Project
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: environmental project
type: Ontology Class
---

# environmental project

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject>

## Definition

specific initiative, activity, or investment aimed at improving environmental sustainability, reducing ecological harm, or addressing environmental challenges

## Relationships

- **Subclass of**: [Project](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Project.md)

## Constraints

- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: some values from of type [MilestoneSchedule](/concepts/fibo/FND/Agreements/Contracts/MilestoneSchedule.md)
- **[hasAssessmentBoundary](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/hasAssessmentBoundary.md)**: min qualified cardinality 0 of type [AssessmentBoundary](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/AssessmentBoundary.md)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: some values from of type [SustainabilityKeyPerformanceIndicator](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator.md)
- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: min qualified cardinality 0 of type [EnvironmentalProgram](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/EnvironmentalProgram.md)

## Annotations

- **label**: environmental project
- **definition**: specific initiative, activity, or investment aimed at improving environmental sustainability, reducing ecological harm, or addressing environmental challenges
- **explanatoryNote**: Key characteristics of an environmental or sustainability project include achieving measurable positive environmental outcomes, and aligning with broader sustainability goals, such as those outlined in international frameworks (e.g., the United Nations Sustainable Development Goals (SDGs), Paris Agreement).
- **explanatoryNote**: Such projects are designed to align with environmental goals, such as mitigating climate change, conserving natural resources, protecting biodiversity, and promoting a circular economy.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
