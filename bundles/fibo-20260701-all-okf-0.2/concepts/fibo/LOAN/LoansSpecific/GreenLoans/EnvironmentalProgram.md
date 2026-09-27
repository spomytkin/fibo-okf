---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: environmental program
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: broad scale initiative, activity, or investment aimed at improving environmental sustainability, reducing ecological
      harm, or addressing environmental challenges
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Key characteristics of an environmental or sustainability program include achieving measurable positive environmental
      outcomes, and aligning with broader sustainability goals, such as those outlined in international frameworks (e.g.,
      the United Nations Sustainable Development Goals (SDGs), Paris Agreement). Large scale environmental programs may consist
      of a number of projects aimed at addressing specific requirements that support the broader challenges outlined under
      the program.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Program.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Program
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/EnvironmentalProgram
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: environmental program
type: Ontology Class
---

# environmental program

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/EnvironmentalProgram>

## Definition

broad scale initiative, activity, or investment aimed at improving environmental sustainability, reducing ecological harm, or addressing environmental challenges

## Relationships

- **Subclass of**: [Program](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Program.md)

## Constraints

- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: some values from of type [SustainabilityKeyPerformanceIndicator](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: min qualified cardinality 0 of type [EnvironmentalProject](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject.md)

## Annotations

- **label**: environmental program
- **definition**: broad scale initiative, activity, or investment aimed at improving environmental sustainability, reducing ecological harm, or addressing environmental challenges
- **explanatoryNote**: Key characteristics of an environmental or sustainability program include achieving measurable positive environmental outcomes, and aligning with broader sustainability goals, such as those outlined in international frameworks (e.g., the United Nations Sustainable Development Goals (SDGs), Paris Agreement). Large scale environmental programs may consist of a number of projects aimed at addressing specific requirements that support the broader challenges outlined under the program.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
