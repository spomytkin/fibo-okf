---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity redemption provision
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: redemption provision that specifies the conditions under which the issuer or shareholder may redeem the shares
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasEarliestRedemptionDate
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExtendableRedemptionDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasMinimumRedemptionPrice
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasRedemptionPremium
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/isRedeemableAtIssuerOption
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/isRedeemableAtShareholderOption
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvision
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: equity redemption provision
type: Ontology Class
---

# equity redemption provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvision>

## Definition

redemption provision that specifies the conditions under which the issuer or shareholder may redeem the shares

## Relationships

- **Subclass of**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)

## Constraints

- **[hasEarliestRedemptionDate](/concepts/fibo/SEC/Equities/EquityInstruments/hasEarliestRedemptionDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasExtendableRedemptionDate](/concepts/fibo/SEC/Equities/EquityInstruments/hasExtendableRedemptionDate.md)**: min qualified cardinality 0 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[hasMinimumRedemptionPrice](/concepts/fibo/SEC/Equities/EquityInstruments/hasMinimumRedemptionPrice.md)**: min qualified cardinality 0 of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **[hasRedemptionPremium](/concepts/fibo/SEC/Equities/EquityInstruments/hasRedemptionPremium.md)**: min qualified cardinality 0 of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **[isRedeemableAtIssuerOption](/concepts/fibo/SEC/Equities/EquityInstruments/isRedeemableAtIssuerOption.md)**: min qualified cardinality 0 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isRedeemableAtShareholderOption](/concepts/fibo/SEC/Equities/EquityInstruments/isRedeemableAtShareholderOption.md)**: min qualified cardinality 0 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): equity redemption provision
- **definition** (en): redemption provision that specifies the conditions under which the issuer or shareholder may redeem the shares

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
