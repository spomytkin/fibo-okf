---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity conversion terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: conversion terms specifying the details regarding conversion of shares into other securities
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/specifiesConversionDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/specifiesConversionInto
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/ConversionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConversionTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityConversionTerms
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: equity conversion terms
type: Ontology Class
---

# equity conversion terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityConversionTerms>

## Definition

conversion terms specifying the details regarding conversion of shares into other securities

## Relationships

- **Subclass of**: [ConversionTerms](/concepts/fibo/SEC/Securities/SecuritiesIssuance/ConversionTerms.md)

## Constraints

- **[specifiesConversionDate](/concepts/fibo/SEC/Equities/EquityInstruments/specifiesConversionDate.md)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[specifiesConversionInto](/concepts/fibo/SEC/Securities/SecuritiesIssuance/specifiesConversionInto.md)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label**: equity conversion terms
- **definition**: conversion terms specifying the details regarding conversion of shares into other securities

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
