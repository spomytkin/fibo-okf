---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business recurrence interval
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: recurrence interval that is defined per a specific convention that determines how recurring days should be handled
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessRecurrenceIntervalConvention
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceInterval
sources:
- id: fibo-source-7e287b0092
  resource: references/fibo/FND/DatesAndTimes/BusinessDates.rdf
  sha256: 7e287b0092247d35e3e8e12b9c1c29cba3b2b4f94d06a6b0c06e85f6c1cc2f62
  title: FIBO source FND/DatesAndTimes/BusinessDates.rdf
title: business recurrence interval
type: Ontology Class
---

# business recurrence interval

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceInterval>

## Definition

recurrence interval that is defined per a specific convention that determines how recurring days should be handled

## Relationships

- **Subclass of**: [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)

## Constraints

- **[hasBusinessRecurrenceIntervalConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessRecurrenceIntervalConvention.md)**: exact qualified cardinality 1 of type [BusinessRecurrenceIntervalConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)

## Annotations

- **label**: business recurrence interval
- **definition**: recurrence interval that is defined per a specific convention that determines how recurring days should be handled

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
