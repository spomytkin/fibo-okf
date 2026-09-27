---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tradable fund unit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security representing a tradable interest in a fund
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Tradable fund units typically occur in collective investment schemes such as mutual funds or exchange-traded funds
      (ETFs), where units are bought and sold on regulated markets.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity
  - concept: /concepts/fibo/SEC/Funds/Funds/FundUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/TradableFundUnit
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: tradable fund unit
type: Ontology Class
---

# tradable fund unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/TradableFundUnit>

## Definition

security representing a tradable interest in a fund

## Relationships

- **Subclass of**: [EquityInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument.md)
- **Subclass of**: [NegotiableSecurity](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity.md)
- **Subclass of**: [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Annotations

- **label** (en): tradable fund unit
- **definition** (en): security representing a tradable interest in a fund
- **explanatoryNote**: Tradable fund units typically occur in collective investment schemes such as mutual funds or exchange-traded funds (ETFs), where units are bought and sold on regulated markets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
