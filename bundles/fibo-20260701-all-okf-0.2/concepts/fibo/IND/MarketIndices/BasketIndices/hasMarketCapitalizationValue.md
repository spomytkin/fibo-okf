---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has market capitalization value
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the monetary amount representing the market capitalization of some issuer as of some date
  domain:
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices/MarketCapitalization.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/MarketCapitalization
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasMarketCapitalizationValue
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: has market capitalization value
type: Ontology Property
---

# has market capitalization value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasMarketCapitalizationValue>

## Definition

indicates the monetary amount representing the market capitalization of some issuer as of some date

## Relationships

- **Domain**: [MarketCapitalization](/concepts/fibo/IND/MarketIndices/BasketIndices/MarketCapitalization.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label** (en): has market capitalization value
- **definition** (en): indicates the monetary amount representing the market capitalization of some issuer as of some date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
