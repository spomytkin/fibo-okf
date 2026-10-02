---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has debt ranking
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the ranking of this debt instrument with respect to the credit index as a whole
  domain:
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices/CreditIndexConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndexConstituent
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasDebtRanking
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: has debt ranking
type: Ontology Property
---

# has debt ranking

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasDebtRanking>

## Definition

indicates the ranking of this debt instrument with respect to the credit index as a whole

## Relationships

- **Domain**: [CreditIndexConstituent](/concepts/fibo/IND/MarketIndices/BasketIndices/CreditIndexConstituent.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): has debt ranking
- **definition** (en): indicates the ranking of this debt instrument with respect to the credit index as a whole

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
