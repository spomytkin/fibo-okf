---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has duration of unemployment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the length of time, typically in weeks, that people classified as unemployed have been continuously looking
      for work
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: https://www.bls.gov/cps/definitions.htm
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasDurationOfUnemployment
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: has duration of unemployment
type: Ontology Property
---

# has duration of unemployment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasDurationOfUnemployment>

## Definition

specifies the length of time, typically in weeks, that people classified as unemployed have been continuously looking for work

## Relationships

- **Range**: [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)
- **Related to**: [definitions.htm](<https://www.bls.gov/cps/definitions.htm>)
- **Subproperty of**: [hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)

## Annotations

- **label**: has duration of unemployment
- **definition**: specifies the length of time, typically in weeks, that people classified as unemployed have been continuously looking for work

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
