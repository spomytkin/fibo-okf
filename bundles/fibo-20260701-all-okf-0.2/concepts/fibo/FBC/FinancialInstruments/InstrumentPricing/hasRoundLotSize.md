---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has round lot size
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: standard number of securities traded on an exchange
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In stocks, a round lot is considered 100 shares or a larger number that can be evenly divided by 100. In bonds,
      a round lot is usually $100,000 worth. Odd lots and smaller lots have become increasingly common due to technology advances
      and small investor demand.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: normal trading unit
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: unit of trading
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasLotSize.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasLotSize
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasRoundLotSize
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: has round lot size
type: Ontology Property
---

# has round lot size

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasRoundLotSize>

## Definition

standard number of securities traded on an exchange

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasLotSize](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasLotSize.md)

## Annotations

- **label** (en): has round lot size
- **definition** (en): standard number of securities traded on an exchange
- **explanatoryNote** (en): In stocks, a round lot is considered 100 shares or a larger number that can be evenly divided by 100. In bonds, a round lot is usually $100,000 worth. Odd lots and smaller lots have become increasingly common due to technology advances and small investor demand.
- **synonym** (en): normal trading unit
- **synonym** (en): unit of trading

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
