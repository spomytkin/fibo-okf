---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has reference period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a reference (baseline) recurrence interval for which a given measure applies
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
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReferencePeriod
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has reference period
type: Ontology Property
---

# has reference period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReferencePeriod>

## Definition

specifies a reference (baseline) recurrence interval for which a given measure applies

## Relationships

- **Range**: [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **Subproperty of**: [hasRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval.md)

## Annotations

- **label**: has reference period
- **definition**: specifies a reference (baseline) recurrence interval for which a given measure applies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
