---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has spot exchange rate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rate of exchange between two currencies as specified as of some date and time as quoted by a specific source, typically
      for a spot contract
  range:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/hasQuotedExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasQuotedExchangeRate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/hasSpotExchangeRate
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: has spot exchange rate
type: Ontology Property
---

# has spot exchange rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/hasSpotExchangeRate>

## Definition

rate of exchange between two currencies as specified as of some date and time as quoted by a specific source, typically for a spot contract

## Relationships

- **Range**: [QuotedExchangeRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)
- **Subproperty of**: [hasQuotedExchangeRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/hasQuotedExchangeRate.md)

## Annotations

- **label** (en): has spot exchange rate
- **definition** (en): rate of exchange between two currencies as specified as of some date and time as quoted by a specific source, typically for a spot contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
