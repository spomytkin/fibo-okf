---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: USD-TBILL-H.15-Bloomberg
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: USD-TBILL-H.15-Bloomberg
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented
      through the date on which parties enter into the relevant transaction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isProducedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/USD-TBILL-H.15-Bloomberg
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: USD-TBILL-H.15-Bloomberg
type: Ontology Individual
---

# USD-TBILL-H.15-Bloomberg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/USD-TBILL-H.15-Bloomberg>

## Relationships

- **Related to**: [BoardOfGovernorsOfTheFederalReserveSystem](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem.md)
- **Related to**: [USDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md)
- **Related to**: [BloombergLP](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md)

## Annotations

- **label**: USD-TBILL-H.15-Bloomberg
- **abbreviation**: USD-TBILL-H.15-Bloomberg
- **explanatoryNote**: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
