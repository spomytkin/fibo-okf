---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has original notional value
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the notional amount represented by the index when it is first constituted
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
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasNotionalAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNotionalAmount
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasOriginalNotionalValue
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: has original notional value
type: Ontology Property
---

# has original notional value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasOriginalNotionalValue>

## Definition

indicates the notional amount represented by the index when it is first constituted

## Relationships

- **Domain**: [CreditIndex](/concepts/fibo/IND/MarketIndices/BasketIndices/CreditIndex.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasNotionalAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasNotionalAmount.md)

## Annotations

- **label** (en): has original notional value
- **definition** (en): indicates the notional amount represented by the index when it is first constituted

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
