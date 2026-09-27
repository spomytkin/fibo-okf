---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has call rate basis
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: for each call event on the schedule, indicates whether the rate is expressed as a percentage of par or percentage
      of percentage of cumulative average value (CAV)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Zero coupon bonds and OID bonds are callable at an accreted value.
  domain:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallEvent
  range:
  - concept: /concepts/fibo/SEC/Debt/Bonds/RateBasisConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RateBasisConvention
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasCallRateBasis
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has call rate basis
type: Ontology Property
---

# has call rate basis

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasCallRateBasis>

## Definition

for each call event on the schedule, indicates whether the rate is expressed as a percentage of par or percentage of percentage of cumulative average value (CAV)

## Relationships

- **Domain**: [CallEvent](/concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md)
- **Range**: [RateBasisConvention](/concepts/fibo/SEC/Debt/Bonds/RateBasisConvention.md)

## Annotations

- **label**: has call rate basis
- **definition**: for each call event on the schedule, indicates whether the rate is expressed as a percentage of par or percentage of percentage of cumulative average value (CAV)
- **explanatoryNote**: Zero coupon bonds and OID bonds are callable at an accreted value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
