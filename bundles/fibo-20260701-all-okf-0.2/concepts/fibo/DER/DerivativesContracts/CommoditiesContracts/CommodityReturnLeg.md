---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity return leg
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: leg of a commodity return swap in which the return is based on a physical commodity, or the price, or behavior
      of the price, or any other aspect related to a physical commodity
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The cash flows from a commodity may be negative as you have a cost from holding the commodity but there are no
      interim cash flows, so it equates to a negative interest rate. So a commodity swap is like a TRS in that it is based
      on the return on the increase in value.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/ReturnLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityReturnLeg
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: commodity return leg
type: Ontology Class
---

# commodity return leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityReturnLeg>

## Definition

leg of a commodity return swap in which the return is based on a physical commodity, or the price, or behavior of the price, or any other aspect related to a physical commodity

## Relationships

- **Subclass of**: [ReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/ReturnLeg.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from of type [CommodityDerivativeUnderlier](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier.md)

## Annotations

- **label** (en): commodity return leg
- **definition** (en): leg of a commodity return swap in which the return is based on a physical commodity, or the price, or behavior of the price, or any other aspect related to a physical commodity
- **explanatoryNote** (en): The cash flows from a commodity may be negative as you have a cost from holding the commodity but there are no interim cash flows, so it equates to a negative interest rate. So a commodity swap is like a TRS in that it is based on the return on the increase in value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
