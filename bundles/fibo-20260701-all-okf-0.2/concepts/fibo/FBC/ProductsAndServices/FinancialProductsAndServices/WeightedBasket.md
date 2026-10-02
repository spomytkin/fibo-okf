---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weighted basket
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket whose constituents have some relative importance with respect to one another
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/WeightingFunction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Basket
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/StructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: weighted basket
type: Ontology Class
---

# weighted basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket>

## Definition

basket whose constituents have some relative importance with respect to one another

## Relationships

- **Subclass of**: [Basket](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md)
- **Subclass of**: [StructuredCollection](<https://www.omg.org/spec/Commons/Collections/StructuredCollection>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [WeightedBasketConstituent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md)
- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: some values from of type [WeightingFunction](/concepts/fibo/FND/Utilities/Analytics/WeightingFunction.md)

## Annotations

- **label**: weighted basket
- **definition**: basket whose constituents have some relative importance with respect to one another

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
