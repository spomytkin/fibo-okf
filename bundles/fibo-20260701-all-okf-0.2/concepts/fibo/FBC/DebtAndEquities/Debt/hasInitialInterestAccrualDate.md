---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has initial interest accrual date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the date from which interest begins to accrue
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has dated date
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialInterestAccrualDate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has initial interest accrual date
type: Ontology Property
---

# has initial interest accrual date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialInterestAccrualDate>

## Definition

the date from which interest begins to accrue

## Relationships

- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **Subproperty of**: [hasStartDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate>)

## Annotations

- **label**: has initial interest accrual date
- **definition**: the date from which interest begins to accrue
- **synonym**: has dated date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
