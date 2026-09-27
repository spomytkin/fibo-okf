---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: simple yield calculation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The annual rate of return expressed as a percentage. This is the return divided by the outlay and multiplied by
      100 to express the figure as a percentage.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is yield in its simplest sense, expressed as a percentage of return to outlay. As such, this is the same way
      that yield is determined for any investments, not just financial instruments or debt investments.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/DirtyPrice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/SimpleYieldCalculationMethod
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: simple yield calculation method
type: Ontology Class
---

# simple yield calculation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/SimpleYieldCalculationMethod>

## Definition

The annual rate of return expressed as a percentage. This is the return divided by the outlay and multiplied by 100 to express the figure as a percentage.

## Relationships

- **Subclass of**: [YieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [DirtyPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/DirtyPrice.md)

## Annotations

- **label** (en): simple yield calculation method
- **definition** (en): The annual rate of return expressed as a percentage. This is the return divided by the outlay and multiplied by 100 to express the figure as a percentage.
- **explanatoryNote** (en): This is yield in its simplest sense, expressed as a percentage of return to outlay. As such, this is the same way that yield is determined for any investments, not just financial instruments or debt investments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
