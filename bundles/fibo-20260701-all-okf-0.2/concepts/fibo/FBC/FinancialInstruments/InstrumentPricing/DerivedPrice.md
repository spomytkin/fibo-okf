---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: derived price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: price that stems from another source or calculation rather than being quoted or based on actual trading data
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, a product's price can be derived from another pricing source, such as an asset or product, using various
      contributing factors. Derived prices can also be calculated within a firm using published price spreads or other market
      data. An interpolated price is determined by interpolation between available price figures, using some algorithm or
      curve, such as between bid and offer (among others). It also includes yield curves and implied forward curves. That
      is, interpolation may either be linear (straight line interpolation between two values) or may be expressed as a non
      linear curve such as a yield curve or an implied forward curve.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are evaluated prices in which an independent source evaluates a price they have derived, and there are prices
      which are derived within a firm, from supplied, published end of day price spreads or other market data.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: interpolated price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: matrix price
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/CalculatedPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CalculatedPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/DerivedPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: derived price
type: Ontology Class
---

# derived price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/DerivedPrice>

## Definition

price that stems from another source or calculation rather than being quoted or based on actual trading data

## Relationships

- **Subclass of**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- **Subclass of**: [CalculatedPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/CalculatedPrice.md)

## Annotations

- **label** (en): derived price
- **definition** (en): price that stems from another source or calculation rather than being quoted or based on actual trading data
- **example** (en): For example, a product's price can be derived from another pricing source, such as an asset or product, using various contributing factors. Derived prices can also be calculated within a firm using published price spreads or other market data. An interpolated price is determined by interpolation between available price figures, using some algorithm or curve, such as between bid and offer (among others). It also includes yield curves and implied forward curves. That is, interpolation may either be linear (straight line interpolation between two values) or may be expressed as a non linear curve such as a yield curve or an implied forward curve.
- **explanatoryNote** (en): There are evaluated prices in which an independent source evaluates a price they have derived, and there are prices which are derived within a firm, from supplied, published end of day price spreads or other market data.
- **synonym** (en): interpolated price
- **synonym** (en): matrix price

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
