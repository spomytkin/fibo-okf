---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has method of adjustment
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the method used to address any changes to the contract based on events that occur over the contract lifecycle
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/EquityForward.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/EquityForward
  range:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/ForwardContractAdjustmentMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/ForwardContractAdjustmentMethod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/hasMethodOfAdjustment
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: has method of adjustment
type: Ontology Property
---

# has method of adjustment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/hasMethodOfAdjustment>

## Definition

indicates the method used to address any changes to the contract based on events that occur over the contract lifecycle

## Relationships

- **Domain**: [EquityForward](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/EquityForward.md)
- **Range**: [ForwardContractAdjustmentMethod](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/ForwardContractAdjustmentMethod.md)
- **Subproperty of**: [hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)

## Annotations

- **label** (en): has method of adjustment
- **definition** (en): indicates the method used to address any changes to the contract based on events that occur over the contract lifecycle

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
