---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: day-count convention
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a business recurrence interval convention that is used to calculate the number of days in an interest payment,
      which applies to the amount of accrued interest or the present value for debt instruments
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Day-count conventions apply to swaps, mortgages and forward rate agreements as well as bonds, each of which has
      its own day-count convention, which varies depending on the type of instrument, whether the interest rate is fixed or
      floating, and the country of issuance. Among the most common conventions are 30/360 or 365, actual/360 or 365, and actual/actual.
      A 30/360 convention assumes 30 days in a month and 360 days in a year. An actual/360 convention assumes the actual number
      of days in the given month and 360 days in the year. An actual/ actual convention uses the actual number of days in
      the given interest period and year.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: day-count convention
type: Ontology Class
---

# day-count convention

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention>

## Definition

a business recurrence interval convention that is used to calculate the number of days in an interest payment, which applies to the amount of accrued interest or the present value for debt instruments

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [BusinessRecurrenceIntervalConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Annotations

- **label**: day-count convention
- **definition**: a business recurrence interval convention that is used to calculate the number of days in an interest payment, which applies to the amount of accrued interest or the present value for debt instruments
- **explanatoryNote**: Day-count conventions apply to swaps, mortgages and forward rate agreements as well as bonds, each of which has its own day-count convention, which varies depending on the type of instrument, whether the interest rate is fixed or floating, and the country of issuance. Among the most common conventions are 30/360 or 365, actual/360 or 365, and actual/actual. A 30/360 convention assumes 30 days in a month and 360 days in a year. An actual/360 convention assumes the actual number of days in the given month and 360 days in the year. An actual/ actual convention uses the actual number of days in the given interest period and year.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
