---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: recurrence interval
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: time interval that is consistent between elements of a regular schedule
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: frequency
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/TimeInterval
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: recurrence interval
type: Ontology Class
---

# recurrence interval

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval>

## Definition

time interval that is consistent between elements of a regular schedule

## Relationships

- **Subclass of**: [TimeInterval](<https://www.omg.org/spec/Commons/DatesAndTimes/TimeInterval>)

## Annotations

- **label**: recurrence interval
- **definition**: time interval that is consistent between elements of a regular schedule
- **synonym**: frequency

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
