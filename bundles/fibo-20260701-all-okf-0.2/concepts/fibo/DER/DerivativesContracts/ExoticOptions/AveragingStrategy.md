---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: averaging strategy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: method used for calculating the average rate or price of an Asian option
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AsianOption
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Strategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Strategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AveragingStrategy
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: averaging strategy
type: Ontology Class
---

# averaging strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AveragingStrategy>

## Definition

method used for calculating the average rate or price of an Asian option

## Relationships

- **Subclass of**: [Strategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Strategy.md)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [AsianOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/AsianOption.md)

## Annotations

- **label** (en): averaging strategy
- **definition** (en): method used for calculating the average rate or price of an Asian option

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
