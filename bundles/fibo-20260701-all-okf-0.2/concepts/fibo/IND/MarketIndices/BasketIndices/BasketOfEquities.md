---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket of equities
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of securities whose constituents are listed shares
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: Nac50d4f99c4048a285cf535fafcc20fe
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Baskets/BasketOfSecurities.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfSecurities
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/BasketOfEquities
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: basket of equities
type: Ontology Class
---

# basket of equities

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/BasketOfEquities>

## Definition

basket of securities whose constituents are listed shares

## Relationships

- **Subclass of**: [BasketOfSecurities](/concepts/fibo/SEC/Securities/Baskets/BasketOfSecurities.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `Nac50d4f99c4048a285cf535fafcc20fe`

## Annotations

- **label** (en): basket of equities
- **definition** (en): basket of securities whose constituents are listed shares

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
