---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket of commodities
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: custom basket whose constituents consist of one or more negotiable commodities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019-10
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A commodity basket may contain constituents from one of the potential underlying assets or from multiple underlying
      assets.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityBasketConstituent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/BasketOfCommodities
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: basket of commodities
type: Ontology Class
---

# basket of commodities

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/BasketOfCommodities>

## Definition

custom basket whose constituents consist of one or more negotiable commodities

## Relationships

- **Subclass of**: [WeightedBasket](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [CommodityBasketConstituent](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityBasketConstituent.md)

## Annotations

- **label**: basket of commodities
- **definition**: custom basket whose constituents consist of one or more negotiable commodities
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10
- **explanatoryNote** (en): A commodity basket may contain constituents from one of the potential underlying assets or from multiple underlying assets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
