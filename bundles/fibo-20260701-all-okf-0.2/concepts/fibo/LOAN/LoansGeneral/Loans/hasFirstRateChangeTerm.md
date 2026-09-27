---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has first rate change term
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a period of time in months after origination during which the interest rate cannot change
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: This normally applies to a variable rate loan. It may also apply to step up/step down loans that are fixed rate
      but whose rate changes after a pre-determined number of months.
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasFirstRateChangeTerm
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has first rate change term
type: Ontology Property
---

# has first rate change term

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasFirstRateChangeTerm>

## Definition

specifies a period of time in months after origination during which the interest rate cannot change

## Relationships

- **Subproperty of**: [hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)

## Annotations

- **label**: has first rate change term
- **definition**: specifies a period of time in months after origination during which the interest rate cannot change
- **usageNote**: This normally applies to a variable rate loan. It may also apply to step up/step down loans that are fixed rate but whose rate changes after a pre-determined number of months.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
