---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity basket constituent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: component of a custom commodity basket whose relative importance with respect to other basket constituents is known
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/hasCommodityValueAsOfDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAsOfDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Commodity
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityBasketConstituent
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: commodity basket constituent
type: Ontology Class
---

# commodity basket constituent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityBasketConstituent>

## Definition

component of a custom commodity basket whose relative importance with respect to other basket constituents is known

## Relationships

- **Subclass of**: [WeightedBasketConstituent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md)

## Constraints

- **[hasCommodityValueAsOfDate](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/hasCommodityValueAsOfDate.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasAsOfDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAsOfDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[involves](/concepts/fibo/FND/Relations/Relations/involves.md)**: min qualified cardinality 0 of type [Commodity](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Commodity.md)
- **[hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)**: min qualified cardinality 0 of type [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)

## Annotations

- **label**: commodity basket constituent
- **definition**: component of a custom commodity basket whose relative importance with respect to other basket constituents is known

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
