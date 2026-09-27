---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has relative duration
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: duration between two explicit dates
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A relative duration may be negative.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that this property is distinct from hasDurationValue, as a relative duration may resolve to a relative date
      or date time (both of which are time points) rather than an interval, which would result in a logical inconsistency
      if its parent property is hasDurationValue.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasRelativeDuration
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: has relative duration
type: Ontology Property
---

# has relative duration

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasRelativeDuration>

## Definition

duration between two explicit dates

## Relationships

- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: has relative duration
- **definition**: duration between two explicit dates
- **explanatoryNote**: A relative duration may be negative.
- **explanatoryNote**: Note that this property is distinct from hasDurationValue, as a relative duration may resolve to a relative date or date time (both of which are time points) rather than an interval, which would result in a logical inconsistency if its parent property is hasDurationValue.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
