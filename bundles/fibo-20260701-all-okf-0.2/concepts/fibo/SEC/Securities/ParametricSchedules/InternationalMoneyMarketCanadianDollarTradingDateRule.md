---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: International Money Market (IMM) Canadian Dollar (CAD) trading date rule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trading date rule defined as the last trading day / expiration day of the Canadian Derivatives Exchange (Bourse
      do Montreal Inc.), three month Bankers' Acceptance Futures (Ticker symbol BAX), the second London banking day prior
      to the third Wednesday of the contract month
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: IMM CAD trading date rule
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the determined day is a bourse or bank holiday in Toronto or Montreal, the last trading day shall be the previous
      bank business day, per the Canadian Derivatives Exchange BAX contract specification. The above description implies a
      Date Roll Rule which is presumably referenced by referring to this rule, so that when this rule is referenced, there
      would be no Date Roll Rule defined in the FpML message. Semantically, this is still a Date Roll Rule, specifically a
      "Roll forward" rule with no modification (the third Wednesday of a month will never roll forward to a day in the following
      month so no Modified rule is required).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
    value: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayPreceding
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/ParametricSchedules/TradingDateRule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/TradingDateRule
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/InternationalMoneyMarketCanadianDollarTradingDateRule
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: International Money Market (IMM) Canadian Dollar (CAD) trading date rule
type: Ontology Class
---

# International Money Market (IMM) Canadian Dollar (CAD) trading date rule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/InternationalMoneyMarketCanadianDollarTradingDateRule>

## Definition

trading date rule defined as the last trading day / expiration day of the Canadian Derivatives Exchange (Bourse do Montreal Inc.), three month Bankers' Acceptance Futures (Ticker symbol BAX), the second London banking day prior to the third Wednesday of the contract month

## Relationships

- **Subclass of**: [TradingDateRule](/concepts/fibo/SEC/Securities/ParametricSchedules/TradingDateRule.md)

## Constraints

- **[hasBusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayPreceding`

## Annotations

- **label**: International Money Market (IMM) Canadian Dollar (CAD) trading date rule
- **definition**: trading date rule defined as the last trading day / expiration day of the Canadian Derivatives Exchange (Bourse do Montreal Inc.), three month Bankers' Acceptance Futures (Ticker symbol BAX), the second London banking day prior to the third Wednesday of the contract month
- **abbreviation**: IMM CAD trading date rule
- **explanatoryNote**: If the determined day is a bourse or bank holiday in Toronto or Montreal, the last trading day shall be the previous bank business day, per the Canadian Derivatives Exchange BAX contract specification. The above description implies a Date Roll Rule which is presumably referenced by referring to this rule, so that when this rule is referenced, there would be no Date Roll Rule defined in the FpML message. Semantically, this is still a Date Roll Rule, specifically a "Roll forward" rule with no modification (the third Wednesday of a month will never roll forward to a day in the following month so no Modified rule is required).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
