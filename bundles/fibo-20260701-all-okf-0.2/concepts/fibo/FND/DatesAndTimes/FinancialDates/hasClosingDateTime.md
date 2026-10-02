---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has closing date time
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the day and time at which something closes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: The use of custom datatypes is outside the OWL 2 RL profile and so users should consider commenting out the range
      restriction or change the range to rdfs:Literal in applications that are constrained to OWL 2 RL.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasClosingDateTime
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: has closing date time
type: Ontology Property
---

# has closing date time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasClosingDateTime>

## Definition

the day and time at which something closes

## Relationships

- **Range**: [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **Subproperty of**: [hasObservedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime>)

## Annotations

- **label** (en): has closing date time
- **definition** (en): the day and time at which something closes
- **usageNote**: The use of custom datatypes is outside the OWL 2 RL profile and so users should consider commenting out the range restriction or change the range to rdfs:Literal in applications that are constrained to OWL 2 RL.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
