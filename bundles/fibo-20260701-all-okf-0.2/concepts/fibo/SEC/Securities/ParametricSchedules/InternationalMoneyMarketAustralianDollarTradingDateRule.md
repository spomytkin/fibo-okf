---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: International Money Market (IMM) Australian Dollar (AUD) trading date rule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trading date rule defined as the last trading day of an Australian Stock Exchange (ASX) 90-Day Bank Accepted Futures
      and Options product, one Sydney business day preceding the second Friday of the relevant settlement month
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: IMM AUD trading date rule
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.asx.com.au/documents/products/90-Day-bank-bill-futures-factsheet.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/ParametricSchedules/TradingDateRule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/TradingDateRule
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/InternationalMoneyMarketAustralianDollarTradingDateRule
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: International Money Market (IMM) Australian Dollar (AUD) trading date rule
type: Ontology Class
---

# International Money Market (IMM) Australian Dollar (AUD) trading date rule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/InternationalMoneyMarketAustralianDollarTradingDateRule>

## Definition

trading date rule defined as the last trading day of an Australian Stock Exchange (ASX) 90-Day Bank Accepted Futures and Options product, one Sydney business day preceding the second Friday of the relevant settlement month

## Relationships

- **Subclass of**: [TradingDateRule](/concepts/fibo/SEC/Securities/ParametricSchedules/TradingDateRule.md)

## Annotations

- **label**: International Money Market (IMM) Australian Dollar (AUD) trading date rule
- **definition**: trading date rule defined as the last trading day of an Australian Stock Exchange (ASX) 90-Day Bank Accepted Futures and Options product, one Sydney business day preceding the second Friday of the relevant settlement month
- **abbreviation**: IMM AUD trading date rule
- **adaptedFrom**: http://www.asx.com.au/documents/products/90-Day-bank-bill-futures-factsheet.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
