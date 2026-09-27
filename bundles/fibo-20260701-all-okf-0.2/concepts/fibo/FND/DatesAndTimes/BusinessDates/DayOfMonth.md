---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: day of month
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specific, recurring day of the month
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasOrdinalNumber
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceInterval.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceInterval
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/DayOfMonth
sources:
- id: fibo-source-7e287b0092
  resource: references/fibo/FND/DatesAndTimes/BusinessDates.rdf
  sha256: 7e287b0092247d35e3e8e12b9c1c29cba3b2b4f94d06a6b0c06e85f6c1cc2f62
  title: FIBO source FND/DatesAndTimes/BusinessDates.rdf
title: day of month
type: Ontology Class
---

# day of month

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/DayOfMonth>

## Definition

specific, recurring day of the month

## Relationships

- **Subclass of**: [BusinessRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceInterval.md)

## Constraints

- **[hasOrdinalNumber](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasOrdinalNumber.md)**: exact qualified cardinality 1 of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)

## Annotations

- **label**: day of month
- **definition**: specific, recurring day of the month

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
