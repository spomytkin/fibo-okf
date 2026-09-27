---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has spread range
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the range of credit spread for the constituents of the index
  domain:
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices/CreditIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndex
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasSpreadRange
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: has spread range
type: Ontology Property
---

# has spread range

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasSpreadRange>

## Definition

the range of credit spread for the constituents of the index

## Relationships

- **Domain**: [CreditIndex](/concepts/fibo/IND/MarketIndices/BasketIndices/CreditIndex.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): has spread range
- **definition** (en): the range of credit spread for the constituents of the index

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
