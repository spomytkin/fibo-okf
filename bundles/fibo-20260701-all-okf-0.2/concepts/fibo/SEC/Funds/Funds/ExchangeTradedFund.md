---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exchange-traded fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment fund whose fund units are traded on an exchange, much like stocks
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ETF
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An ETF holds assets such as stocks, commodities, or bonds, and trades close to its net asset value over the course
      of the trading day. Most ETFs track an index, such as a stock, bond, or commodity index.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/Funds/OpenEndInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/OpenEndInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/ExchangeTradedFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: exchange-traded fund
type: Ontology Class
---

# exchange-traded fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/ExchangeTradedFund>

## Definition

investment fund whose fund units are traded on an exchange, much like stocks

## Relationships

- **Subclass of**: [OpenEndInvestment](/concepts/fibo/SEC/Funds/Funds/OpenEndInvestment.md)

## Annotations

- **label** (en): exchange-traded fund
- **definition** (en): investment fund whose fund units are traded on an exchange, much like stocks
- **abbreviation** (en): ETF
- **adaptedFrom** (en): ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, October 2019
- **explanatoryNote** (en): An ETF holds assets such as stocks, commodities, or bonds, and trades close to its net asset value over the course of the trading day. Most ETFs track an index, such as a stock, bond, or commodity index.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
