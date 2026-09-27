---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt instrument yield
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The return on the debt instrument at the stated price.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Yield has a relationship to the price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/calculationFollowing
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasOutlookPeriod
    value: N5fad33bd31e7464f9d918a45e644a0fd
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/Yield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/Yield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: debt instrument yield
type: Ontology Class
---

# debt instrument yield

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield>

## Definition

The return on the debt instrument at the stated price.

## Relationships

- **Subclass of**: [Yield](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/Yield.md)

## Constraints

- **[calculationFollowing](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/calculationFollowing.md)**: some values from of type [YieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)
- **[hasOutlookPeriod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasOutlookPeriod.md)**: some values from value `N5fad33bd31e7464f9d918a45e644a0fd`
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)

## Annotations

- **label** (en): debt instrument yield
- **definition** (en): The return on the debt instrument at the stated price.
- **explanatoryNote** (en): Yield has a relationship to the price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
