---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency volatility option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: currency option whose underlying asset is based on the volatility of a foreign exchange rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nf112f2b5996f43fa8520edeede3b42ef
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyVolatilityOption
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: currency volatility option
type: Ontology Class
---

# currency volatility option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyVolatilityOption>

## Definition

currency option whose underlying asset is based on the volatility of a foreign exchange rate

## Relationships

- **Subclass of**: [CurrencyOption](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyOption.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nf112f2b5996f43fa8520edeede3b42ef`

## Annotations

- **label** (en): currency volatility option
- **definition** (en): currency option whose underlying asset is based on the volatility of a foreign exchange rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
