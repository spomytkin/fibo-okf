---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: performance determination timeframe
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The timeframe on which the performance is reported (e.g. 1month, 1 year, YTD).
  domain:
  - concept: /concepts/fibo/MD/CIVTemporal/FundsTemporal/PerformanceDeterminationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/PerformanceDeterminationMethod
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/performanceDeterminationTimeframe
sources:
- id: fibo-source-6355d85024
  resource: references/fibo/MD/CIVTemporal/FundsTemporal.rdf
  sha256: 6355d85024e646fcee8b117a329d3c2307126ca0c3e3721b62ec12813bf12817
  title: FIBO source MD/CIVTemporal/FundsTemporal.rdf
title: performance determination timeframe
type: Ontology Property
---

# performance determination timeframe

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/performanceDeterminationTimeframe>

## Definition

The timeframe on which the performance is reported (e.g. 1month, 1 year, YTD).

## Relationships

- **Domain**: [PerformanceDeterminationMethod](/concepts/fibo/MD/CIVTemporal/FundsTemporal/PerformanceDeterminationMethod.md)
- **Range**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label** (en): performance determination timeframe
- **definition** (en): The timeframe on which the performance is reported (e.g. 1month, 1 year, YTD).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
