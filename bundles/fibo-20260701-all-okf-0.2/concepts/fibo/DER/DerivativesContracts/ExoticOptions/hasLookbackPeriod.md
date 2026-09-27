---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has lookback period
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: window of time during which the lookback is effective
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasLookbackPeriod
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: has lookback period
type: Ontology Property
---

# has lookback period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasLookbackPeriod>

## Definition

window of time during which the lookback is effective

## Relationships

- **Domain**: [LookbackStrikeTerms](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms.md)
- **Range**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **Subproperty of**: [hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)

## Annotations

- **label** (en): has lookback period
- **definition** (en): window of time during which the lookback is effective

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
