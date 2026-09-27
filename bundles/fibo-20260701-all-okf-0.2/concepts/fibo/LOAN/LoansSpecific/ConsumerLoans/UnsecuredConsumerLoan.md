---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unsecured consumer loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan to one or more individuals for household, family, or other personal expenditures granted based on the strength
      of the borrower's credit history or reputation in the community
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/UnsecuredLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/UnsecuredLoan
  - concept: /concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/ConsumerLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/ConsumerLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/UnsecuredConsumerLoan
sources:
- id: fibo-source-7c7642cd54
  resource: references/fibo/LOAN/LoansSpecific/ConsumerLoans.rdf
  sha256: 7c7642cd546c2c1de619d2ea9b384b314886dedf7c8601dab9a46870d0e591d7
  title: FIBO source LOAN/LoansSpecific/ConsumerLoans.rdf
title: unsecured consumer loan
type: Ontology Class
---

# unsecured consumer loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/UnsecuredConsumerLoan>

## Definition

loan to one or more individuals for household, family, or other personal expenditures granted based on the strength of the borrower's credit history or reputation in the community

## Relationships

- **Subclass of**: [UnsecuredLoan](/concepts/fibo/LOAN/LoansGeneral/Loans/UnsecuredLoan.md)
- **Subclass of**: [ConsumerLoan](/concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/ConsumerLoan.md)

## Annotations

- **label** (en): unsecured consumer loan
- **definition** (en): loan to one or more individuals for household, family, or other personal expenditures granted based on the strength of the borrower's credit history or reputation in the community

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
