---
owl:
  annotations:
  - language: en-GB
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: programme
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: program
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: state of affairs and coordinated set of activities designed to obtain benefits not available from managing them
      individually
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.prince2.com/usa/blog/project-vs-programme
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Goal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasGoal
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Objective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Project
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasDescription
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/ProgramName
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasName
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/ProgramIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Program
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: program
type: Ontology Class
---

# program

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Program>

## Definition

state of affairs and coordinated set of activities designed to obtain benefits not available from managing them individually

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[hasGoal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasGoal.md)**: min qualified cardinality 0 of type [Goal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Goal.md)
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [Objective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Objective.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: min qualified cardinality 0 of type [Project](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Project.md)
- **[hasDescription](<https://www.omg.org/spec/Commons/Designators/hasDescription>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasName](<https://www.omg.org/spec/Commons/Designators/hasName>)**: min qualified cardinality 0 of type [ProgramName](/concepts/fibo/FND/GoalsAndObjectives/Objectives/ProgramName.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [ProgramIdentifier](/concepts/fibo/FND/GoalsAndObjectives/Objectives/ProgramIdentifier.md)

## Annotations

- **label** (en-GB): programme
- **label** (en-US): program
- **definition**: state of affairs and coordinated set of activities designed to obtain benefits not available from managing them individually
- **adaptedFrom**: https://www.prince2.com/usa/blog/project-vs-programme

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
