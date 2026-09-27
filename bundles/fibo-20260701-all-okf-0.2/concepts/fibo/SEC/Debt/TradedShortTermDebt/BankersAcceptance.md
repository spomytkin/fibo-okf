---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bankers' acceptance
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: short-term debt instrument that is guaranteed and paid by a bank and used as a relatively safe form of payment
      for large transactions
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Considered negotiable instruments with features of a time draft, bankers' acceptances are created by the drawer
      and provide the bearer with the right to the amount noted on the face of the acceptance on the specified date. Unlike
      traditional checks, bankers' acceptances function based on the creditworthiness of the banking institution instead of
      the individual or business acting as the drawer. Additionally, the drawer must provide the funds necessary to support
      the bankers' acceptance, eliminating the risk associated with insufficient funds on the part of the drawer.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasGuarantor
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/AtADiscount
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt/BillOfExchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/BillOfExchange
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/BankersAcceptance
sources:
- id: fibo-source-5edf240c05
  resource: references/fibo/SEC/Debt/TradedShortTermDebt.rdf
  sha256: 5edf240c05ec5ae1a2890d6bacd728412073d70868c0908cad8aaea54d9d21bf
  title: FIBO source SEC/Debt/TradedShortTermDebt.rdf
title: bankers' acceptance
type: Ontology Class
---

# bankers' acceptance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/BankersAcceptance>

## Definition

short-term debt instrument that is guaranteed and paid by a bank and used as a relatively safe form of payment for large transactions

## Relationships

- **Subclass of**: [BillOfExchange](/concepts/fibo/SEC/Debt/TradedShortTermDebt/BillOfExchange.md)

## Constraints

- **[hasGuarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/hasGuarantor.md)**: some values from of type [Bank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md)
- **[hasRelativePriceAtIssue](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/AtADiscount`
- **[hasRelativePriceAtMaturity](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue`

## Annotations

- **label** (en): bankers' acceptance
- **definition** (en): short-term debt instrument that is guaranteed and paid by a bank and used as a relatively safe form of payment for large transactions
- **explanatoryNote** (en): Considered negotiable instruments with features of a time draft, bankers' acceptances are created by the drawer and provide the bearer with the right to the amount noted on the face of the acceptance on the specified date. Unlike traditional checks, bankers' acceptances function based on the creditworthiness of the banking institution instead of the individual or business acting as the drawer. Additionally, the drawer must provide the funds necessary to support the bankers' acceptance, eliminating the risk associated with insufficient funds on the part of the drawer.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
