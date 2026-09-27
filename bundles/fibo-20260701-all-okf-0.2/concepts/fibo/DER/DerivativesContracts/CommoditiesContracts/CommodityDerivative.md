---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity derivative
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument whose primary underlying item is a physical commodity, or the price, or related index, or
      any other aspect related to a physical commodity
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The price of any commodity used as the basis for a commodity derivative may vary according to supply and demand
      as of the execution date of the contract and at various other times during the lifetime of the contract depending on
      contract terms. Valuation of a commodity derivative may depend on the spot price for the underlying commodity, futures
      price, supply and demand, convenience yield, cost of money and/or interest rates, volatility, which models were used
      to predict future pricing, and so forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: commodity derivative
type: Ontology Class
---

# commodity derivative

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative>

## Definition

derivative instrument whose primary underlying item is a physical commodity, or the price, or related index, or any other aspect related to a physical commodity

## Relationships

- **Subclass of**: [CommodityInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument.md)
- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: min qualified cardinality 0 of type [CommodityDerivativeUnderlier](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier.md)

## Annotations

- **label**: commodity derivative
- **definition** (en): derivative instrument whose primary underlying item is a physical commodity, or the price, or related index, or any other aspect related to a physical commodity
- **explanatoryNote** (en): The price of any commodity used as the basis for a commodity derivative may vary according to supply and demand as of the execution date of the contract and at various other times during the lifetime of the contract depending on contract terms. Valuation of a commodity derivative may depend on the spot price for the underlying commodity, futures price, supply and demand, convenience yield, cost of money and/or interest rates, volatility, which models were used to predict future pricing, and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
