---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commodity derivative that includes, without limitation, any swap for which the primary underlying notional item
      is a physical commodity, or the price, or behavior of the price, or the level of a commodity index, or other aspect
      related to a physical commodity
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: CFTC glossary
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019-10
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Commodities that can be swapped include: energy. metal, agriculture, environmental, freight, polypropylene products,
      fertilizer, paper, single and multiple commodity indexes and baskets, and multi-commodity assets where each leg references
      a different commodity.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Commodity swaps typically involve the exchange of a floating commodity price for a set price over an agreed-upon
      period.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityReturnLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasReturnLeg
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommoditySwap
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: commodity swap
type: Ontology Class
---

# commodity swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommoditySwap>

## Definition

commodity derivative that includes, without limitation, any swap for which the primary underlying notional item is a physical commodity, or the price, or behavior of the price, or the level of a commodity index, or other aspect related to a physical commodity

## Relationships

- **Subclass of**: [CommodityDerivative](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- **Subclass of**: [ReturnSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md)

## Constraints

- **[hasReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasReturnLeg.md)**: some values from of type [CommodityReturnLeg](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityReturnLeg.md)

## Annotations

- **label** (en): commodity swap
- **definition** (en): commodity derivative that includes, without limitation, any swap for which the primary underlying notional item is a physical commodity, or the price, or behavior of the price, or the level of a commodity index, or other aspect related to a physical commodity
- **adaptedFrom** (en): CFTC glossary
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10
- **explanatoryNote** (en): Commodities that can be swapped include: energy. metal, agriculture, environmental, freight, polypropylene products, fertilizer, paper, single and multiple commodity indexes and baskets, and multi-commodity assets where each leg references a different commodity.
- **explanatoryNote** (en): Commodity swaps typically involve the exchange of a floating commodity price for a set price over an agreed-upon period.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
