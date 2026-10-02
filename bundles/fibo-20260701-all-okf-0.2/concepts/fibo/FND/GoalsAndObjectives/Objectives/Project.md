---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: project
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: state of affairs and unique and temporary organization, designed to deliver a tangible output
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.prince2.com/usa/blog/project-vs-programme
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A project has a fixed - generally fairly short - timeframe, and a project manager is responsible for delivering
      the output on time and on budget.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - cardinality: 0
    kind: min_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOutput
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Goal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasGoal
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Objective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Program
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasDescription
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/ProjectName
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasName
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/ProjectIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Project
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: project
type: Ontology Class
---

# project

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Project>

## Definition

state of affairs and unique and temporary organization, designed to deliver a tangible output

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: min cardinality 0
- **[hasOutput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOutput.md)**: min cardinality 0
- **[hasGoal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasGoal.md)**: min qualified cardinality 0 of type [Goal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Goal.md)
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [Objective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Objective.md)
- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: min qualified cardinality 0 of type [Program](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Program.md)
- **[hasDescription](<https://www.omg.org/spec/Commons/Designators/hasDescription>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasName](<https://www.omg.org/spec/Commons/Designators/hasName>)**: min qualified cardinality 0 of type [ProjectName](/concepts/fibo/FND/GoalsAndObjectives/Objectives/ProjectName.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [ProjectIdentifier](/concepts/fibo/FND/GoalsAndObjectives/Objectives/ProjectIdentifier.md)

## Annotations

- **label**: project
- **definition**: state of affairs and unique and temporary organization, designed to deliver a tangible output
- **adaptedFrom**: https://www.prince2.com/usa/blog/project-vs-programme
- **explanatoryNote** (en): A project has a fixed - generally fairly short - timeframe, and a project manager is responsible for delivering the output on time and on budget.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
