---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: aim
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: intention specifying a desired direction, condition, or situation toward which an agent's actions are directed,
      without requiring precise scope or measurable criteria
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Business aims are sometimes considered broad, long-term goals, and in such cases, the term 'aim' is used interchangeably
      with goal. Here, however we differentiate between qualitative goals and quantitative objectives, both of which are kinds
      of aims, with the critical differences including measurability and time frame. Goals tend to have a much longer trajectory,
      provide the basis for determining objectives, and are often aligned with an organization's mission, whereas objectives
      are short term and measurable.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Approach
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/isAddressedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Aim
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: aim
type: Ontology Class
---

# aim

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Aim>

## Definition

intention specifying a desired direction, condition, or situation toward which an agent's actions are directed, without requiring precise scope or measurable criteria

## Constraints

- **[isAddressedBy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/isAddressedBy.md)**: min qualified cardinality 0 of type [Approach](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Approach.md)

## Annotations

- **label**: aim
- **definition**: intention specifying a desired direction, condition, or situation toward which an agent's actions are directed, without requiring precise scope or measurable criteria
- **explanatoryNote**: Business aims are sometimes considered broad, long-term goals, and in such cases, the term 'aim' is used interchangeably with goal. Here, however we differentiate between qualitative goals and quantitative objectives, both of which are kinds of aims, with the critical differences including measurability and time frame. Goals tend to have a much longer trajectory, provide the basis for determining objectives, and are often aligned with an organization's mission, whereas objectives are short term and measurable.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
