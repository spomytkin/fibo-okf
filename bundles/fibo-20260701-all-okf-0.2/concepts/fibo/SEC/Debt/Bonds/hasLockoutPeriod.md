---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has lockout period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the period of time for which a callable security cannot be called and only interest coupon payments are
      received by the security holder
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: With a 10-year noncall 3-year ("10nc3") debt security, the security cannot be called for the first three years.
  domain:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasLockoutPeriod
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has lockout period
type: Ontology Property
---

# has lockout period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasLockoutPeriod>

## Definition

indicates the period of time for which a callable security cannot be called and only interest coupon payments are received by the security holder

## Relationships

- **Domain**: [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)
- **Range**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **Subproperty of**: [hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)

## Annotations

- **label**: has lockout period
- **definition**: indicates the period of time for which a callable security cannot be called and only interest coupon payments are received by the security holder
- **example**: With a 10-year noncall 3-year ("10nc3") debt security, the security cannot be called for the first three years.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
