---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: objective
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: aim distinguished by specific scope and measurable criteria, often quantitative and short-term that a party seeks
      to attain, typically in order to achieve its long-term goals
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Goal
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Aim.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Aim
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Objective
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: objective
type: Ontology Class
---

# objective

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Objective>

## Definition

aim distinguished by specific scope and measurable criteria, often quantitative and short-term that a party seeks to attain, typically in order to achieve its long-term goals

## Relationships

- **Subclass of**: [Aim](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Aim.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: min qualified cardinality 0 of type [Goal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Goal.md)
- **[hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)**: min qualified cardinality 0 of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label**: objective
- **definition**: aim distinguished by specific scope and measurable criteria, often quantitative and short-term that a party seeks to attain, typically in order to achieve its long-term goals

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
