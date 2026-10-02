---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: EUR-3M EURIBOR SWAP-EUREX vs LCH-ICAP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: EUR-3M EURIBOR SWAP-EUREX vs LCH-ICAP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented
      through the date on which parties enter into the relevant transaction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Euro.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/Euro
  - concept: /concepts/fibo/IND/InterestRates/InterestRates/ThreeMonths.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasTenor
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ThreeMonths
  - concept: /concepts/fibo/IND/InterestRates/MarketDataProviders/EuropeanMoneyMarketsInstituteBenchmarkPublisher.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isProducedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/EuropeanMoneyMarketsInstituteBenchmarkPublisher
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/EUR-3M_EURIBOR_SWAP-EUREX_vs_LCH-ICAP
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: EUR-3M EURIBOR SWAP-EUREX vs LCH-ICAP
type: Ontology Individual
---

# EUR-3M EURIBOR SWAP-EUREX vs LCH-ICAP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/EUR-3M_EURIBOR_SWAP-EUREX_vs_LCH-ICAP>

## Relationships

- **Related to**: [EuropeanMoneyMarketsInstituteBenchmarkPublisher](/concepts/fibo/IND/InterestRates/MarketDataProviders/EuropeanMoneyMarketsInstituteBenchmarkPublisher.md)
- **Related to**: [Euro](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Euro.md)
- **Related to**: [ThreeMonths](/concepts/fibo/IND/InterestRates/InterestRates/ThreeMonths.md)

## Annotations

- **label**: EUR-3M EURIBOR SWAP-EUREX vs LCH-ICAP
- **abbreviation**: EUR-3M EURIBOR SWAP-EUREX vs LCH-ICAP
- **explanatoryNote**: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
