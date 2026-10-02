---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has as-of date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something to the date on which it is accurate or valid (e.g. a credit report has an asOfDate that means
      the date when the information was drawn)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: It is different from the creation date and need not be the last date of the DatePeriod covered.
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAsOfDate
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: has as-of date
type: Ontology Property
---

# has as-of date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAsOfDate>

## Definition

relates something to the date on which it is accurate or valid (e.g. a credit report has an asOfDate that means the date when the information was drawn)

## Relationships

- **Subproperty of**: [hasDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDate>)

## Annotations

- **label**: has as-of date
- **definition**: relates something to the date on which it is accurate or valid (e.g. a credit report has an asOfDate that means the date when the information was drawn)
- **explanatoryNote**: It is different from the creation date and need not be the last date of the DatePeriod covered.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
