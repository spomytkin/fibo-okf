---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has total points and fees
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a form of pre-paid interest, charged by the lender as an alternative to charging a higher rate of interest
      on the mortgage loan
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: One point equals one percent of the loan principal, and usually reduces the interest rate by 1/8 percent (0.125)
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/hasCost.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasCost
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasTotalPointsAndFees
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has total points and fees
type: Ontology Property
---

# has total points and fees

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasTotalPointsAndFees>

## Definition

indicates a form of pre-paid interest, charged by the lender as an alternative to charging a higher rate of interest on the mortgage loan

## Relationships

- **Subproperty of**: [hasCost](/concepts/fibo/LOAN/LoansGeneral/Loans/hasCost.md)

## Annotations

- **label**: has total points and fees
- **definition**: indicates a form of pre-paid interest, charged by the lender as an alternative to charging a higher rate of interest on the mortgage loan
- **explanatoryNote**: One point equals one percent of the loan principal, and usually reduces the interest rate by 1/8 percent (0.125)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
