---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has loan balance
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the balance with respect to the principal on the loan as of some date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/hasOutstandingAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasOutstandingAmount
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasLoanBalance
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has loan balance
type: Ontology Property
---

# has loan balance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasLoanBalance>

## Definition

indicates the balance with respect to the principal on the loan as of some date

## Relationships

- **Subproperty of**: [hasOutstandingAmount](/concepts/fibo/FBC/DebtAndEquities/Debt/hasOutstandingAmount.md)
- **Subproperty of**: [hasBalance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance.md)

## Annotations

- **label**: has loan balance
- **definition**: indicates the balance with respect to the principal on the loan as of some date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
