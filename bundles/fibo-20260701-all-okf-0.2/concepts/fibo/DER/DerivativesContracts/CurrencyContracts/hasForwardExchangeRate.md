---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has forward exchange rate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rate of exchange between two currencies as specified in a forward contract
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyForward.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForward
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/ExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/ExchangeRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/hasForwardExchangeRate
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: has forward exchange rate
type: Ontology Property
---

# has forward exchange rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/hasForwardExchangeRate>

## Definition

rate of exchange between two currencies as specified in a forward contract

## Relationships

- **Domain**: [CurrencyForward](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyForward.md)
- **Range**: [ExchangeRate](/concepts/fibo/FND/Accounting/CurrencyAmount/ExchangeRate.md)
- **Subproperty of**: [hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)

## Annotations

- **label** (en): has forward exchange rate
- **definition** (en): rate of exchange between two currencies as specified in a forward contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
