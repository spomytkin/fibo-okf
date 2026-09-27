---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is assumable
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether or not another borrower may assume the payments on this loan
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isAssumable
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: is assumable
type: Ontology Property
---

# is assumable

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isAssumable>

## Definition

indicates whether or not another borrower may assume the payments on this loan

## Relationships

- **Domain**: [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is assumable
- **definition** (en): indicates whether or not another borrower may assume the payments on this loan

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
