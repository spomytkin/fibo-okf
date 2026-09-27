---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: strategy
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: high-level approach that guides decision-making and the coordination of actions and plans in pursuit of some aim
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A strategy is a high-level plan or approach designed to achieve a long-term goal or outcome, often by choosing
      among different possible methods or courses of action. A strategy may involve activities that are needed in order to
      achieve specific goals or objectives. It may take into account one or more policies or any number of restrictions and
      constraints. Strategies are typically distinguished by long-term orientation, adaptive planning, and broad scope.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Goal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasGoal
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Approach.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Approach
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Strategy
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: strategy
type: Ontology Class
---

# strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Strategy>

## Definition

high-level approach that guides decision-making and the coordination of actions and plans in pursuit of some aim

## Relationships

- **Subclass of**: [Approach](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Approach.md)

## Constraints

- **[hasGoal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasGoal.md)**: min qualified cardinality 0 of type [Goal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Goal.md)

## Annotations

- **label**: strategy
- **definition**: high-level approach that guides decision-making and the coordination of actions and plans in pursuit of some aim
- **explanatoryNote** (en): A strategy is a high-level plan or approach designed to achieve a long-term goal or outcome, often by choosing among different possible methods or courses of action. A strategy may involve activities that are needed in order to achieve specific goals or objectives. It may take into account one or more policies or any number of restrictions and constraints. Strategies are typically distinguished by long-term orientation, adaptive planning, and broad scope.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
