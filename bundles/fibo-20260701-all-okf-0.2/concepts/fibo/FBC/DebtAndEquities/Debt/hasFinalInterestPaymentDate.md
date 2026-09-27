---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has final interest payment date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the date on which the last interest payment is due
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasFinalInterestPaymentDate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has final interest payment date
type: Ontology Property
---

# has final interest payment date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasFinalInterestPaymentDate>

## Definition

the date on which the last interest payment is due

## Relationships

- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **Subproperty of**: [hasEndDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate>)

## Annotations

- **label**: has final interest payment date
- **definition**: the date on which the last interest payment is due

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
