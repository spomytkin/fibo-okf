---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has balloon payment
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the contractual terms include or would have included repayment of the outstanding principal sum
      at the end of a loan period, prior to which only partial or no payments were made on the principal
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasBalloonPayment
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has balloon payment
type: Ontology Property
---

# has balloon payment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasBalloonPayment>

## Definition

indicates whether the contractual terms include or would have included repayment of the outstanding principal sum at the end of a loan period, prior to which only partial or no payments were made on the principal

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): has balloon payment
- **definition** (en): indicates whether the contractual terms include or would have included repayment of the outstanding principal sum at the end of a loan period, prior to which only partial or no payments were made on the principal

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
