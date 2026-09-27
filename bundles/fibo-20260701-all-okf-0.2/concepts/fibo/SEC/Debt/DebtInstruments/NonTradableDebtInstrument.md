---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-tradable debt instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a debt instrument that may not be bought or sold
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Low-risk instruments such as savings bonds are examples of nonnegotiable debt instruments.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Generally, a nonnegotiable instrument may be redeemed by the issuer, but this is often subject to some limitations.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasRedemptionProvision
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/RelativePrice
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/RelativePrice
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtRedemption
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/NonTradableDebtInstrument
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: non-tradable debt instrument
type: Ontology Class
---

# non-tradable debt instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/NonTradableDebtInstrument>

## Definition

a debt instrument that may not be bought or sold

## Relationships

- **Subclass of**: [DebtInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)
- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **Disjoint with**: [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
- **[hasRedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasRedemptionProvision.md)**: min qualified cardinality 0 of type [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- **[hasRelativePriceAtIssue](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue.md)**: some values from of type [RelativePrice](/concepts/fibo/SEC/Debt/DebtInstruments/RelativePrice.md)
- **[hasRelativePriceAtRedemption](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtRedemption.md)**: some values from of type [RelativePrice](/concepts/fibo/SEC/Debt/DebtInstruments/RelativePrice.md)

## Annotations

- **label**: non-tradable debt instrument
- **definition**: a debt instrument that may not be bought or sold
- **example**: Low-risk instruments such as savings bonds are examples of nonnegotiable debt instruments.
- **explanatoryNote**: Generally, a nonnegotiable instrument may be redeemed by the issuer, but this is often subject to some limitations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
