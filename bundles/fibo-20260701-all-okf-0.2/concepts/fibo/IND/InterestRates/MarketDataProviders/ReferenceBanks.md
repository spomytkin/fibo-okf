---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reference banks
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: market data provider of interest rate benchmarks representing a group of one or more banks that either individually,
      or in aggregate, provide quoted rates that contribute to the benchmark
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: With respect to LIBOR, for example, the Bank of England will request the principal London office of each of the
      Reference Banks to provide a quotation of its rate. If at least two such quotations are provided, the rate for such
      date will be the arithmetic mean of the quotations. If fewer than two quotations are provided as requested, the rate
      for such date will be the arithmetic mean of the rates quoted by major banks in New York City selected by the Bank,
      at approximately 11:00 a.m. New York City time for loans in U.S. Dollars to leading European banks for such Interest
      Period and in an amount approximately equal to the amount requested LIBOR-Reference Banks Loan.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
  - https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/ReferenceBanks
sources:
- id: fibo-source-0b5fde6ab3
  resource: references/fibo/IND/InterestRates/MarketDataProviders.rdf
  sha256: 0b5fde6ab3fe477e8381e86968420d93073a53e8b18733937a275f845b4e18c4
  title: FIBO source IND/InterestRates/MarketDataProviders.rdf
title: reference banks
type: Ontology Individual
---

# reference banks

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/ReferenceBanks>

## Definition

market data provider of interest rate benchmarks representing a group of one or more banks that either individually, or in aggregate, provide quoted rates that contribute to the benchmark

## Annotations

- **label**: reference banks
- **definition**: market data provider of interest rate benchmarks representing a group of one or more banks that either individually, or in aggregate, provide quoted rates that contribute to the benchmark
- **explanatoryNote**: With respect to LIBOR, for example, the Bank of England will request the principal London office of each of the Reference Banks to provide a quotation of its rate. If at least two such quotations are provided, the rate for such date will be the arithmetic mean of the quotations. If fewer than two quotations are provided as requested, the rate for such date will be the arithmetic mean of the rates quoted by major banks in New York City selected by the Bank, at approximately 11:00 a.m. New York City time for loans in U.S. Dollars to leading European banks for such Interest Period and in an amount approximately equal to the amount requested LIBOR-Reference Banks Loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
