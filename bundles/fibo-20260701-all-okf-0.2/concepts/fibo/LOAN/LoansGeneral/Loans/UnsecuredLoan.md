---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unsecured loan
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan granted based on the strength of the borrower's credit history or reputation in the community
  disjoint_with:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/SecuredLoan.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/SecuredLoan
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/UnsecuredLoan
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: unsecured loan
type: Ontology Class
---

# unsecured loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/UnsecuredLoan>

## Definition

loan granted based on the strength of the borrower's credit history or reputation in the community

## Relationships

- **Subclass of**: [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)

## Constraints

- **Disjoint with**: [SecuredLoan](/concepts/fibo/LOAN/LoansGeneral/Loans/SecuredLoan.md)

## Annotations

- **label**: unsecured loan
- **definition**: loan granted based on the strength of the borrower's credit history or reputation in the community

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
