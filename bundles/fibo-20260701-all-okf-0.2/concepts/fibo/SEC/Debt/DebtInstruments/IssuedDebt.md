---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issued debt
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt that is set out by the borrower in some form of financial security in which the lender is the holder or counterparty
      of that security
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasDebtAmount
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/IssuedDebt
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: issued debt
type: Ontology Class
---

# issued debt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/IssuedDebt>

## Definition

debt that is set out by the borrower in some form of financial security in which the lender is the holder or counterparty of that security

## Relationships

- **Subclass of**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md)

## Constraints

- **[hasDebtAmount](/concepts/fibo/FBC/DebtAndEquities/Debt/hasDebtAmount.md)**: all values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: all values from of type [DebtInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)

## Annotations

- **label**: issued debt
- **definition**: debt that is set out by the borrower in some form of financial security in which the lender is the holder or counterparty of that security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
