---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument representing an ownership interest in bulk goods, such as raw materials and primary agricultural
      products
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The value of the contract is derived from the market value of an underlying commodity or commodity index. Commodity
      derivatives can be physically or cash settled. Primary underliers include metals, agricultural goods and energy.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasCommodityValueAsOfExecutionDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Commodity
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: commodity instrument
type: Ontology Class
---

# commodity instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument>

## Definition

financial instrument representing an ownership interest in bulk goods, such as raw materials and primary agricultural products

## Relationships

- **Subclass of**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Constraints

- **[hasCommodityValueAsOfExecutionDate](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasCommodityValueAsOfExecutionDate.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[involves](/concepts/fibo/FND/Relations/Relations/involves.md)**: min qualified cardinality 0 of type [Commodity](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Commodity.md)
- **[hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)**: min qualified cardinality 0 of type [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)

## Annotations

- **label**: commodity instrument
- **definition**: financial instrument representing an ownership interest in bulk goods, such as raw materials and primary agricultural products
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10.
- **explanatoryNote**: The value of the contract is derived from the market value of an underlying commodity or commodity index. Commodity derivatives can be physically or cash settled. Primary underliers include metals, agricultural goods and energy.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
