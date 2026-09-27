---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has business day convention
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a convention regarding how a date should be handled when it falls on a day that is not a business day,
      such as a weekend or holiday
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
sources:
- id: fibo-source-7e287b0092
  resource: references/fibo/FND/DatesAndTimes/BusinessDates.rdf
  sha256: 7e287b0092247d35e3e8e12b9c1c29cba3b2b4f94d06a6b0c06e85f6c1cc2f62
  title: FIBO source FND/DatesAndTimes/BusinessDates.rdf
title: has business day convention
type: Ontology Property
---

# has business day convention

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention>

## Definition

identifies a convention regarding how a date should be handled when it falls on a day that is not a business day, such as a weekend or holiday

## Relationships

- **Range**: [BusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md)

## Annotations

- **label**: has business day convention
- **definition**: identifies a convention regarding how a date should be handled when it falls on a day that is not a business day, such as a weekend or holiday

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
