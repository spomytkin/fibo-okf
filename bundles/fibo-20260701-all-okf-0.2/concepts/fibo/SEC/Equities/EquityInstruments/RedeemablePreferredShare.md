---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: redeemable preferred share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share that gives the issuer the right to redeem the stock under specified conditions
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasRedemptionProvision
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: redeemable preferred share
type: Ontology Class
---

# redeemable preferred share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShare>

## Definition

preferred share that gives the issuer the right to redeem the stock under specified conditions

## Relationships

- **Subclass of**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)

## Constraints

- **[hasRedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasRedemptionProvision.md)**: some values from of type [EquityRedemptionProvision](/concepts/fibo/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md)

## Annotations

- **label**: redeemable preferred share
- **definition**: preferred share that gives the issuer the right to redeem the stock under specified conditions

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
