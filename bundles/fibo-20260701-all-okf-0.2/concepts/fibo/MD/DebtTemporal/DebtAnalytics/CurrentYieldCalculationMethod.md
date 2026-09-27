---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: current yield calculation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The ratio of the interest payment amount to the clean price.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is a kind of yield that applies to debt instruments only as it relates to the clean price. It differs from
      the simple yield in that simple yield relates to the actual price paid for the bond, which on will differ from the clean
      price by the amount of accrued interest.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/CleanPrice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/CurrentYieldCalculationMethod
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: current yield calculation method
type: Ontology Class
---

# current yield calculation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/CurrentYieldCalculationMethod>

## Definition

The ratio of the interest payment amount to the clean price.

## Relationships

- **Subclass of**: [YieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [CleanPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/CleanPrice.md)

## Annotations

- **label** (en): current yield calculation method
- **definition** (en): The ratio of the interest payment amount to the clean price.
- **explanatoryNote** (en): This is a kind of yield that applies to debt instruments only as it relates to the clean price. It differs from the simple yield in that simple yield relates to the actual price paid for the bond, which on will differ from the clean price by the amount of accrued interest.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
