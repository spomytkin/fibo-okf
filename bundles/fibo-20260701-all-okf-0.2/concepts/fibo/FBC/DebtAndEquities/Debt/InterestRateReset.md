---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate reset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event reflecting a potential adjustment to an interest rate, typically corresponding to a change in the underlying
      benchmark interest rate or index specified in the contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that depending on the contract, a rate reset can occur daily or on some other timetable, and depending on
      the underlying benchmark, the actual rate may or may not change. Rate resets may be associated with variable interest
      rate loans, scheduled reset dates for loans and other debt instruments, for example, interest rate swaps, certain kinds
      of bonds, and the like. The date on which interest is (re)calculated may be an explicit or date relative.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/InterestCalculation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestCalculation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateReset
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: interest rate reset
type: Ontology Class
---

# interest rate reset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateReset>

## Definition

event reflecting a potential adjustment to an interest rate, typically corresponding to a change in the underlying benchmark interest rate or index specified in the contract

## Relationships

- **Subclass of**: [InterestCalculation](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestCalculation.md)

## Annotations

- **label**: interest rate reset
- **definition**: event reflecting a potential adjustment to an interest rate, typically corresponding to a change in the underlying benchmark interest rate or index specified in the contract
- **explanatoryNote**: Note that depending on the contract, a rate reset can occur daily or on some other timetable, and depending on the underlying benchmark, the actual rate may or may not change. Rate resets may be associated with variable interest rate loans, scheduled reset dates for loans and other debt instruments, for example, interest rate swaps, certain kinds of bonds, and the like. The date on which interest is (re)calculated may be an explicit or date relative.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
