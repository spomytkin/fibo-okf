---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trade identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters identifying a trade within some context
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Note that a given trade may consist of multiple transactions, and thus there may be multiple identifiers for such
      transactions associated with a specific trade.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: trade identifier
type: Ontology Class
---

# trade identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier>

## Definition

sequence of characters identifying a trade within some context

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [Trade](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)

## Annotations

- **label**: trade identifier
- **definition**: sequence of characters identifying a trade within some context
- **note**: Note that a given trade may consist of multiple transactions, and thus there may be multiple identifiers for such transactions associated with a specific trade.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
