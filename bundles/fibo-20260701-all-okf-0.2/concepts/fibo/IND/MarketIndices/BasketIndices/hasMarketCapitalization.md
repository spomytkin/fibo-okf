---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has market capitalization
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the market capitalization of some issuer as of some date
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/ShareIssuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ShareIssuer
  range:
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices/MarketCapitalization.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/MarketCapitalization
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasMarketCapitalization
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: has market capitalization
type: Ontology Property
---

# has market capitalization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasMarketCapitalization>

## Definition

indicates the market capitalization of some issuer as of some date

## Relationships

- **Domain**: [ShareIssuer](/concepts/fibo/SEC/Equities/EquityInstruments/ShareIssuer.md)
- **Range**: [MarketCapitalization](/concepts/fibo/IND/MarketIndices/BasketIndices/MarketCapitalization.md)

## Annotations

- **label** (en): has market capitalization
- **definition** (en): indicates the market capitalization of some issuer as of some date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
