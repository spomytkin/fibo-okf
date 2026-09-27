---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: secured consumer loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan to one or more individuals for household, family, or other personal expenditures in which the borrower pledges
      some asset via a security agreement as collateral for the loan, or that is secured via third-party guarantee
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/SecuredLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/SecuredLoan
  - concept: /concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/ConsumerLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/ConsumerLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan
sources:
- id: fibo-source-7c7642cd54
  resource: references/fibo/LOAN/LoansSpecific/ConsumerLoans.rdf
  sha256: 7c7642cd546c2c1de619d2ea9b384b314886dedf7c8601dab9a46870d0e591d7
  title: FIBO source LOAN/LoansSpecific/ConsumerLoans.rdf
title: secured consumer loan
type: Ontology Class
---

# secured consumer loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan>

## Definition

loan to one or more individuals for household, family, or other personal expenditures in which the borrower pledges some asset via a security agreement as collateral for the loan, or that is secured via third-party guarantee

## Relationships

- **Subclass of**: [SecuredLoan](/concepts/fibo/LOAN/LoansGeneral/Loans/SecuredLoan.md)
- **Subclass of**: [ConsumerLoan](/concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/ConsumerLoan.md)

## Annotations

- **label** (en): secured consumer loan
- **definition** (en): loan to one or more individuals for household, family, or other personal expenditures in which the borrower pledges some asset via a security agreement as collateral for the loan, or that is secured via third-party guarantee

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
