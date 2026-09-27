---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment strategy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: plan, method, or series of maneuvers or stratagems for obtaining a specific investment goal
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/InvestmentObjective
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/BusinessStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/InvestmentStrategy
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: investment strategy
type: Ontology Class
---

# investment strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/InvestmentStrategy>

## Definition

plan, method, or series of maneuvers or stratagems for obtaining a specific investment goal

## Relationships

- **Subclass of**: [BusinessStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessStrategy.md)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: some values from of type [InvestmentObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/InvestmentObjective.md)

## Annotations

- **label** (en): investment strategy
- **definition** (en): plan, method, or series of maneuvers or stratagems for obtaining a specific investment goal

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
