---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has index name
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a formal name for the index
  domain:
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices/ReferenceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/ReferenceIndex
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/hasFormalName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasIndexName
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: has index name
type: Ontology Property
---

# has index name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasIndexName>

## Definition

specifies a formal name for the index

## Relationships

- **Domain**: [ReferenceIndex](/concepts/fibo/IND/MarketIndices/BasketIndices/ReferenceIndex.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)
- **Subproperty of**: [hasFormalName](/concepts/fibo/FND/Relations/Relations/hasFormalName.md)

## Annotations

- **label** (en): has index name
- **definition** (en): specifies a formal name for the index

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
