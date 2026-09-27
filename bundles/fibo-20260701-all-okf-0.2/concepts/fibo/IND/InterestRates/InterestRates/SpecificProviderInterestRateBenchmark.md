---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: specific-provider interest rate benchmark
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest rate benchmark that is made available by a specific market data provider for reference purposes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Benchmarks, such as those published by Bloomberg, Thomson-Reuters, and others, are usually quoted as of a specific
      date and time of day.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/IND/InterestRates/InterestRates/InterestRateBenchmark.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/SpecificProviderInterestRateBenchmark
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: specific-provider interest rate benchmark
type: Ontology Class
---

# specific-provider interest rate benchmark

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/SpecificProviderInterestRateBenchmark>

## Definition

interest rate benchmark that is made available by a specific market data provider for reference purposes

## Relationships

- **Subclass of**: [InterestRateBenchmark](/concepts/fibo/IND/InterestRates/InterestRates/InterestRateBenchmark.md)

## Constraints

- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: exact qualified cardinality 1 of type [MarketDataProvider](/concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md)

## Annotations

- **label**: specific-provider interest rate benchmark
- **definition**: interest rate benchmark that is made available by a specific market data provider for reference purposes
- **explanatoryNote**: Benchmarks, such as those published by Bloomberg, Thomson-Reuters, and others, are usually quoted as of a specific date and time of day.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
