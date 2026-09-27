---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: preferred share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share that pays dividends at a specified rate and has preference over common shares in the payment of dividends
      and liquidation of corporate assets
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: preference share
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasMaturityDate
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividend
    value: Nf592494661814d6180a1fc7f56898fe4
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CommonShare
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/isSeniorTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: preferred share
type: Ontology Class
---

# preferred share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare>

## Definition

share that pays dividends at a specified rate and has preference over common shares in the payment of dividends and liquidation of corporate assets

## Relationships

- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Constraints

- **[hasMaturityDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasMaturityDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasDividend](/concepts/fibo/SEC/Equities/EquityInstruments/hasDividend.md)**: some values from value `Nf592494661814d6180a1fc7f56898fe4`
- **[isSeniorTo](/concepts/fibo/SEC/Equities/EquityInstruments/isSeniorTo.md)**: some values from of type [CommonShare](/concepts/fibo/SEC/Equities/EquityInstruments/CommonShare.md)

## Annotations

- **label**: preferred share
- **definition**: share that pays dividends at a specified rate and has preference over common shares in the payment of dividends and liquidation of corporate assets
- **synonym**: preference share

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
