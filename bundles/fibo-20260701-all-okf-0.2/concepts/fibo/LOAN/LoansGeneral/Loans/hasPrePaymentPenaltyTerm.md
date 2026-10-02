---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has pre-payment penalty term
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a loan to a period of time in months after which there is no prepayment penalty
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: A value of zero means no prepayment penalty; this avoids need for a separate boolean property about whether there
      is a prepayment penalty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasPrePaymentPenaltyTerm
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has pre-payment penalty term
type: Ontology Property
---

# has pre-payment penalty term

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasPrePaymentPenaltyTerm>

## Definition

relates a loan to a period of time in months after which there is no prepayment penalty

## Relationships

- **Subproperty of**: [hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)

## Annotations

- **label**: has pre-payment penalty term
- **definition**: relates a loan to a period of time in months after which there is no prepayment penalty
- **usageNote**: A value of zero means no prepayment penalty; this avoids need for a separate boolean property about whether there is a prepayment penalty

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
