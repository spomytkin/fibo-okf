---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trader
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that engages in the transfer of financial assets in any financial market on behalf of a client or the financial
      services provider
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/facilitates
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N42bfd299e1ed482a8680d50b899cf4b5
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trader
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: trader
type: Ontology Class
---

# trader

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trader>

## Definition

party that engages in the transfer of financial assets in any financial market on behalf of a client or the financial services provider

## Relationships

- **Subclass of**: [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)

## Constraints

- **[facilitates](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/facilitates.md)**: some values from of type [Trade](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N42bfd299e1ed482a8680d50b899cf4b5`

## Annotations

- **label**: trader
- **definition**: party that engages in the transfer of financial assets in any financial market on behalf of a client or the financial services provider

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
