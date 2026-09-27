---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has corresponding account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a credit agreement to an account used as the basis for managing transactions
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/relatesTo.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/relatesTo
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasCorrespondingAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: has corresponding account
type: Ontology Property
---

# has corresponding account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasCorrespondingAccount>

## Definition

relates a credit agreement to an account used as the basis for managing transactions

## Relationships

- **Domain**: [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- **Range**: [LoanOrCreditAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md)
- **Subproperty of**: [relatesTo](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/relatesTo.md)

## Annotations

- **label**: has corresponding account
- **definition**: relates a credit agreement to an account used as the basis for managing transactions

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
