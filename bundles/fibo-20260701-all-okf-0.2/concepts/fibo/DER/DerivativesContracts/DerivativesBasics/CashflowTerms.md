---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cashflow terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms setting out a cashflow structure of payments committed to by one party to a contract
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Swap cashflows are known as Swapstreams and are the terms for payment to and from either party. These are defined
      in swap transaction messages and represent the terms of the contract implied by that transaction. Options (Nordea reviews):
      Cashflows are defined as Payouts. This is not the same as a model of a cashflow which is a consequence of applying some
      legal term for payment of interest or principal, but is a commitment expressed in purely cashflow terms. Review this
      though. Payout terms include: Values - values can only go up or down; Static values are defined for limits and the like.
      i.e. Constraints (and direction) - this covers caps and floors - these are read upward or downward Conditionality Formula
      relations (Input and Output): - these are values - these may have a cap or a floor on them also - these also may have
      Multiplication - there is also fixed margin - may have addition or substraction between these Linearity in covered in
      the above Timing / expiry Observaton (not terms): Probability Sensitivity'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DebtTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CashflowTerms
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: cashflow terms
type: Ontology Class
---

# cashflow terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CashflowTerms>

## Definition

terms setting out a cashflow structure of payments committed to by one party to a contract

## Relationships

- **Subclass of**: [DerivativeTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- **Subclass of**: [DebtTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md)

## Annotations

- **label**: cashflow terms
- **definition**: terms setting out a cashflow structure of payments committed to by one party to a contract
- **editorialNote**: Swap cashflows are known as Swapstreams and are the terms for payment to and from either party. These are defined in swap transaction messages and represent the terms of the contract implied by that transaction. Options (Nordea reviews): Cashflows are defined as Payouts. This is not the same as a model of a cashflow which is a consequence of applying some legal term for payment of interest or principal, but is a commitment expressed in purely cashflow terms. Review this though. Payout terms include: Values - values can only go up or down; Static values are defined for limits and the like. i.e. Constraints (and direction) - this covers caps and floors - these are read upward or downward Conditionality Formula relations (Input and Output): - these are values - these may have a cap or a floor on them also - these also may have Multiplication - there is also fixed margin - may have addition or substraction between these Linearity in covered in the above Timing / expiry Observaton (not terms): Probability Sensitivity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
