---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: http://www.w3.org/2002/07/owl#deprecated
    value: 'true'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Deprecated usage: "HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR" code has been deprecated in supplement 79 to
      the 2006 ISDA definitions (Removal of certain Hong Kong Rate Options.). The code is kept in FpML for backward compatibility
      purposes.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented
      through the date on which parties enter into the relevant transaction.
  deprecated: true
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/HongKongDollar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/HongKongDollar
  - concept: /concepts/fibo/IND/InterestRates/InterestRates/ThreeMonths.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasTenor
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ThreeMonths
  - concept: /concepts/fibo/IND/InterestRates/MarketDataProviders/FenicsMarketData.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/FenicsMarketData
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/HKD-Quarterly-Annual_Swap_Rate-4_00-BGCANTOR
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR
type: Ontology Individual
---

# HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/HKD-Quarterly-Annual_Swap_Rate-4_00-BGCANTOR>

## Relationships

- **Related to**: [HongKongDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/HongKongDollar.md)
- **Related to**: [ThreeMonths](/concepts/fibo/IND/InterestRates/InterestRates/ThreeMonths.md)
- **Related to**: [FenicsMarketData](/concepts/fibo/IND/InterestRates/MarketDataProviders/FenicsMarketData.md)

## Annotations

- **label**: HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR
- **deprecated**: true
- **abbreviation**: HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR
- **explanatoryNote**: Deprecated usage: "HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR" code has been deprecated in supplement 79 to the 2006 ISDA definitions (Removal of certain Hong Kong Rate Options.). The code is kept in FpML for backward compatibility purposes.
- **explanatoryNote**: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
