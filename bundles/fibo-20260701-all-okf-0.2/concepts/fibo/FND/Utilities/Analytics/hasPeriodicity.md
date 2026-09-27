---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has periodicity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a recurrence interval (monthly, quarterly, annual) that a statistical measure reflects
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasPeriodicity
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has periodicity
type: Ontology Property
---

# has periodicity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasPeriodicity>

## Definition

specifies a recurrence interval (monthly, quarterly, annual) that a statistical measure reflects

## Relationships

- **Range**: [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **Subproperty of**: [hasRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval.md)

## Annotations

- **label**: has periodicity
- **definition**: specifies a recurrence interval (monthly, quarterly, annual) that a statistical measure reflects

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
