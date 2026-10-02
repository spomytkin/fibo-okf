---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket constituent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: component of a basket
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Basket
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isConstituentOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Constituent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/BasketConstituent
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: basket constituent
type: Ontology Class
---

# basket constituent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/BasketConstituent>

## Definition

component of a basket

## Relationships

- **Subclass of**: [Constituent](<https://www.omg.org/spec/Commons/Collections/Constituent>)

## Constraints

- **[isConstituentOf](<https://www.omg.org/spec/Commons/Collections/isConstituentOf>)**: some values from of type [Basket](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md)

## Annotations

- **label**: basket constituent
- **definition**: component of a basket

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
