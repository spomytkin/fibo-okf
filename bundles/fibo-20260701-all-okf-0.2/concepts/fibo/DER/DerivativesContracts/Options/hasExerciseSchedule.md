---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has exercise schedule
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links an option to the schedule specified in the contract that constrains when it may be exercised
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An exercise schedule may be as simple as a single date or date period. However, in more complex cases, it may be
      an ad hoc schedule of individual dates, or a regular schedule of periodic exercise dates.
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExerciseSchedule
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: has exercise schedule
type: Ontology Property
---

# has exercise schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExerciseSchedule>

## Definition

links an option to the schedule specified in the contract that constrains when it may be exercised

## Relationships

- **Domain**: [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)
- **Range**: [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)
- **Subproperty of**: [hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)

## Annotations

- **label** (en): has exercise schedule
- **definition** (en): links an option to the schedule specified in the contract that constrains when it may be exercised
- **explanatoryNote** (en): An exercise schedule may be as simple as a single date or date period. However, in more complex cases, it may be an ad hoc schedule of individual dates, or a regular schedule of periodic exercise dates.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
