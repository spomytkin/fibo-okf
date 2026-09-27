---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has intended loan purpose
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the purpose to which the loaned funds are to be put
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplication.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplication
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasIntendedLoanPurpose
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: has intended loan purpose
type: Ontology Property
---

# has intended loan purpose

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasIntendedLoanPurpose>

## Definition

indicates the purpose to which the loaned funds are to be put

## Relationships

- **Domain**: [LoanApplication](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplication.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): has intended loan purpose
- **definition** (en): indicates the purpose to which the loaned funds are to be put

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
