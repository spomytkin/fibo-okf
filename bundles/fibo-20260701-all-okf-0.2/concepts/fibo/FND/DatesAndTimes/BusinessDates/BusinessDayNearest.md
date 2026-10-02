---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business day nearest
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: convention specifying that a non-business date will be adjusted to the nearest day that is a business day -- i.e.
      if the non-business day falls on any day other than a Sunday or a Monday, it will be the first preceding day that is
      a business day, and will be the first following business day if it falls on a Sunday or a Monday
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: FPML 5.1 "BusinessDayConventionEnum"
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayNearest
sources:
- id: fibo-source-7e287b0092
  resource: references/fibo/FND/DatesAndTimes/BusinessDates.rdf
  sha256: 7e287b0092247d35e3e8e12b9c1c29cba3b2b4f94d06a6b0c06e85f6c1cc2f62
  title: FIBO source FND/DatesAndTimes/BusinessDates.rdf
title: business day nearest
type: Ontology Individual
---

# business day nearest

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayNearest>

## Definition

convention specifying that a non-business date will be adjusted to the nearest day that is a business day -- i.e. if the non-business day falls on any day other than a Sunday or a Monday, it will be the first preceding day that is a business day, and will be the first following business day if it falls on a Sunday or a Monday

## Annotations

- **label**: business day nearest
- **definition**: convention specifying that a non-business date will be adjusted to the nearest day that is a business day -- i.e. if the non-business day falls on any day other than a Sunday or a Monday, it will be the first preceding day that is a business day, and will be the first following business day if it falls on a Sunday or a Monday
- **adaptedFrom**: FPML 5.1 "BusinessDayConventionEnum"

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
