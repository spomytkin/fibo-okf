---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: calculated price
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: monetary price determined by a formula
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PricingModel
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/uses
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CalculatedPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: calculated price
type: Ontology Class
---

# calculated price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CalculatedPrice>

## Definition

monetary price determined by a formula

## Relationships

- **Subclass of**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Constraints

- **[uses](<https://www.omg.org/spec/Commons/ContextualDesignators/uses>)**: min qualified cardinality 0 of type [PricingModel](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PricingModel.md)
- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: exact qualified cardinality 1 of type [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Annotations

- **label**: calculated price
- **definition**: monetary price determined by a formula

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
