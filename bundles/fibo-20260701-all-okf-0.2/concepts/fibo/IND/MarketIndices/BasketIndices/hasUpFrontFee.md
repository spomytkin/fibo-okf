---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has up front fee
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a fee payable by any party that wishes to participate in a contract based on the index after the start
      of its life
  domain:
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices/CreditIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndex
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasUpFrontFee
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: has up front fee
type: Ontology Property
---

# has up front fee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasUpFrontFee>

## Definition

specifies a fee payable by any party that wishes to participate in a contract based on the index after the start of its life

## Relationships

- **Domain**: [CreditIndex](/concepts/fibo/IND/MarketIndices/BasketIndices/CreditIndex.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): has up front fee
- **definition** (en): specifies a fee payable by any party that wishes to participate in a contract based on the index after the start of its life

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
