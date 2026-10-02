---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: producer price index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing measure of the rate of change over time in the prices of goods and services bought
      and sold by producers
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: PPI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.imf.org/external/pubs/ft/ppi/2010/manual/ppi.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Statistical agencies implement the Laspeyres index by putting it into price-relative (price change from the base
      period) and revenue-share (from the base period) format. In this form, the Laspeyres index can be written as the sum
      of base-period revenue shares of the items in the index times their corresponding price relatives. Statistical agency
      practice has introduced some approximations to the theoretical Laspeyres target due to a number of practical problems
      with producing the Laspeyres index exactly. For these and other pragmatic reasons, some agencies use alternatives depending
      on circumstances. See the IMF publication cited for a full explanation of the most commonly used approaches and trade-offs
      made for determining PPI.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The standard methodology for a typical PPI is based on a Laspeyres price index with fixed quantities from an earlier
      base period. The construction of this index can be thought of in terms of selecting a basket of goods and services representative
      of base-period revenues, valuing this at base-period prices, and then repricing the same basket at current-period prices.
      The target PPI in this case is defined to be the ratio of these two revenues. Practicing statisticians use this methodology
      because it has at least three practical advantages. It is easily explained to the public, it can use often expensive
      and untimely weighting information from the date of the last (or an even earlier) survey or administrative source (rather
      than requiring sources of data for the current month), and it need not be revised if users accept the Laspeyres premise.
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/FixedBasket
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation
    value: N0fc46ba20f7245318457b37c7aa4a9af
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: producer price index
type: Ontology Class
---

# producer price index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex>

## Definition

economic indicator representing measure of the rate of change over time in the prices of goods and services bought and sold by producers

## Relationships

- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **Disjoint with**: [ConsumerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md)
- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: some values from of type [FixedBasket](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/FixedBasket.md)
- **[hasBaselinePopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation.md)**: some values from value `N0fc46ba20f7245318457b37c7aa4a9af`

## Annotations

- **label**: producer price index
- **definition**: economic indicator representing measure of the rate of change over time in the prices of goods and services bought and sold by producers
- **abbreviation**: PPI
- **adaptedFrom**: https://www.imf.org/external/pubs/ft/ppi/2010/manual/ppi.pdf
- **explanatoryNote**: Statistical agencies implement the Laspeyres index by putting it into price-relative (price change from the base period) and revenue-share (from the base period) format. In this form, the Laspeyres index can be written as the sum of base-period revenue shares of the items in the index times their corresponding price relatives. Statistical agency practice has introduced some approximations to the theoretical Laspeyres target due to a number of practical problems with producing the Laspeyres index exactly. For these and other pragmatic reasons, some agencies use alternatives depending on circumstances. See the IMF publication cited for a full explanation of the most commonly used approaches and trade-offs made for determining PPI.
- **explanatoryNote**: The standard methodology for a typical PPI is based on a Laspeyres price index with fixed quantities from an earlier base period. The construction of this index can be thought of in terms of selecting a basket of goods and services representative of base-period revenues, valuing this at base-period prices, and then repricing the same basket at current-period prices. The target PPI in this case is defined to be the ratio of these two revenues. Practicing statisticians use this methodology because it has at least three practical advantages. It is easily explained to the public, it can use often expensive and untimely weighting information from the date of the last (or an even earlier) survey or administrative source (rather than requiring sources of data for the current month), and it need not be revised if users accept the Laspeyres premise.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
