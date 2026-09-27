---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: approach
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: way of addressing an aim or problem characterized by high-level planning and systematic execution, without presupposing
      scope or granularity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Aim
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/addresses
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Objective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Approach
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: approach
type: Ontology Class
---

# approach

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Approach>

## Definition

way of addressing an aim or problem characterized by high-level planning and systematic execution, without presupposing scope or granularity

## Constraints

- **[addresses](/concepts/fibo/FND/GoalsAndObjectives/Objectives/addresses.md)**: min qualified cardinality 0 of type [Aim](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Aim.md)
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [Objective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Objective.md)

## Annotations

- **label**: approach
- **definition**: way of addressing an aim or problem characterized by high-level planning and systematic execution, without presupposing scope or granularity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
