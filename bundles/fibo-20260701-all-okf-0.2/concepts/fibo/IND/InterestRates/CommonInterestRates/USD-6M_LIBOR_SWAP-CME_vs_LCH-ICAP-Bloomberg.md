---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: USD-6M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: USD-6M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg
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
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar
  - concept: /concepts/fibo/IND/InterestRates/InterestRates/SixMonths.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasTenor
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/SixMonths
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/USD-6M_LIBOR_SWAP-CME_vs_LCH-ICAP-Bloomberg
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: USD-6M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg
type: Ontology Individual
---

# USD-6M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/USD-6M_LIBOR_SWAP-CME_vs_LCH-ICAP-Bloomberg>

## Relationships

- **Related to**: [USDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md)
- **Related to**: [SixMonths](/concepts/fibo/IND/InterestRates/InterestRates/SixMonths.md)
- **Related to**: [BloombergLP](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md)

## Annotations

- **label**: USD-6M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg
- **abbreviation**: USD-6M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg
- **explanatoryNote**: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
