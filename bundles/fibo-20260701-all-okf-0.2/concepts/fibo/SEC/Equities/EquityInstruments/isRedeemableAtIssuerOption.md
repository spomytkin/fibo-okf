---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is redeemable at issuer option
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the issuer has the option of initiating the buy-back, similar to a call feature
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/isRedeemableAtIssuerOption
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: is redeemable at issuer option
type: Ontology Property
---

# is redeemable at issuer option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/isRedeemableAtIssuerOption>

## Definition

indicates whether the issuer has the option of initiating the buy-back, similar to a call feature

## Relationships

- **Domain**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is redeemable at issuer option
- **definition**: indicates whether the issuer has the option of initiating the buy-back, similar to a call feature

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
