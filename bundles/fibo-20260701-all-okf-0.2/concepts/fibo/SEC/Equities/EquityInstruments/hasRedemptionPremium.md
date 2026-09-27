---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has redemption premium
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the premium price per share over the market price, if any, that must be paid in order to redeem the stock
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvision
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasRedemptionPremium
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has redemption premium
type: Ontology Property
---

# has redemption premium

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasRedemptionPremium>

## Definition

indicates the premium price per share over the market price, if any, that must be paid in order to redeem the stock

## Relationships

- **Domain**: [EquityRedemptionProvision](/concepts/fibo/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md)
- **Range**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **Subproperty of**: [hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)

## Annotations

- **label**: has redemption premium
- **definition**: indicates the premium price per share over the market price, if any, that must be paid in order to redeem the stock

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
