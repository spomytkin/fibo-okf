---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond future
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: futures contract whose underlying asset is at least one bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N9f766bd6b43f485ba69618647508c24e
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/DebtInstrumentFuture.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/DebtInstrumentFuture
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/BondFuture
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: bond future
type: Ontology Class
---

# bond future

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/BondFuture>

## Definition

futures contract whose underlying asset is at least one bond

## Relationships

- **Subclass of**: [DebtInstrumentFuture](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/DebtInstrumentFuture.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N9f766bd6b43f485ba69618647508c24e`

## Annotations

- **label** (en): bond future
- **definition** (en): futures contract whose underlying asset is at least one bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
