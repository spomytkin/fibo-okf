---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: repurchase agreement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: agreement between two parties whereby one party lends the other a security at a specified price with a commitment
      to take the security back at a later date for another specified price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: REPO
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Most repos are overnight transactions, with the sale taking place one day and being reversed the next day. Long-term
      repos - called term repos - can extend for a month or more. Usually, repos are for a fixed period of time, but open-ended
      deals are also possible. Reverse repo is a term used to describe the opposite side of a repo transaction. The party
      who sells and later repurchases a security is said to perform a repo. The other party - who purchases and later resells
      the security - is said to perform a reverse repo. While a repo functions like the sale and subsequent repurchase of
      a security, but the legal reality and the economic effect is that of a secured loan. This is a loan as the original
      owner retains the rights to the cashflows of the underlying security. Economically, the party purchasing the security
      makes funds available to the seller and holds the security as collateral. If the repurchased security pays a dividend,
      coupon or partial redemptions during the repo, the funds are returned to the original owner. The difference between
      the sale and repurchase prices paid for the security represent interest on the loan. Indeed, repos are quoted as interest
      rates. A repo always pays interest at maturity, i.e. there are no periodic interest payments.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/RepurchaseAgreement
sources:
- id: fibo-source-5edf240c05
  resource: references/fibo/SEC/Debt/TradedShortTermDebt.rdf
  sha256: 5edf240c05ec5ae1a2890d6bacd728412073d70868c0908cad8aaea54d9d21bf
  title: FIBO source SEC/Debt/TradedShortTermDebt.rdf
title: repurchase agreement
type: Ontology Class
---

# repurchase agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/RepurchaseAgreement>

## Definition

agreement between two parties whereby one party lends the other a security at a specified price with a commitment to take the security back at a later date for another specified price

## Relationships

- **Subclass of**: [MoneyMarketInstrument](/concepts/fibo/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md)

## Constraints

- **[hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)**: max qualified cardinality 1 of type [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)

## Annotations

- **label** (en): repurchase agreement
- **definition** (en): agreement between two parties whereby one party lends the other a security at a specified price with a commitment to take the security back at a later date for another specified price
- **abbreviation** (en): REPO
- **explanatoryNote** (en): Most repos are overnight transactions, with the sale taking place one day and being reversed the next day. Long-term repos - called term repos - can extend for a month or more. Usually, repos are for a fixed period of time, but open-ended deals are also possible. Reverse repo is a term used to describe the opposite side of a repo transaction. The party who sells and later repurchases a security is said to perform a repo. The other party - who purchases and later resells the security - is said to perform a reverse repo. While a repo functions like the sale and subsequent repurchase of a security, but the legal reality and the economic effect is that of a secured loan. This is a loan as the original owner retains the rights to the cashflows of the underlying security. Economically, the party purchasing the security makes funds available to the seller and holds the security as collateral. If the repurchased security pays a dividend, coupon or partial redemptions during the repo, the funds are returned to the original owner. The difference between the sale and repurchase prices paid for the security represent interest on the loan. Indeed, repos are quoted as interest rates. A repo always pays interest at maturity, i.e. there are no periodic interest payments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
