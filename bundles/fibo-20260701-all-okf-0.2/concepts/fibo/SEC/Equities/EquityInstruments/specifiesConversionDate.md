---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: specifies conversion date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date on which, or after which, conversion may occur
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/EquityConversionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityConversionTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/specifiesConversionDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: specifies conversion date
type: Ontology Property
---

# specifies conversion date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/specifiesConversionDate>

## Definition

indicates the date on which, or after which, conversion may occur

## Relationships

- **Domain**: [EquityConversionTerms](/concepts/fibo/SEC/Equities/EquityInstruments/EquityConversionTerms.md)
- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: specifies conversion date
- **definition**: indicates the date on which, or after which, conversion may occur

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
