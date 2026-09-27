---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Kuna
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: http://www.w3.org/2002/07/owl#deprecated
    value: 'true'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the currency Kuna
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Effective 1 Jan 2023, Croatia will use the Euro as its primary currency. The Kuna (HRK) and Euro (EUR) will be
      used during the parallel circulation period from 1 January 2023 to 14 January 2023 inclusive. The period of mandatory
      dual price display lasts from 5 September 2022 to 31 December 2023. As of 1 January 2023, the Kuna should be listed
      as the old/historic currency of Croatia. The exchange rate is fixed at EUR 1 = HRK 7.53450
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
    value: '2'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
    value: '191'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Kuna (HRK) will be retained in FIBO at least through 2023 due to the possibility of dual listing and to support
      instrument pricing that predated this change.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Kuna
  deprecated: true
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
  related_to:
  - predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Croatia
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/Kuna
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: Kuna
type: Ontology Individual
---

# Kuna

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/Kuna>

## Definition

the currency Kuna

## Relationships

- **Related to**: [Croatia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Croatia>)

## Annotations

- **label**: Kuna
- **deprecated**: true
- **definition** (en): the currency Kuna
- **note**: Effective 1 Jan 2023, Croatia will use the Euro as its primary currency. The Kuna (HRK) and Euro (EUR) will be used during the parallel circulation period from 1 January 2023 to 14 January 2023 inclusive. The period of mandatory dual price display lasts from 5 September 2022 to 31 December 2023. As of 1 January 2023, the Kuna should be listed as the old/historic currency of Croatia. The exchange rate is fixed at EUR 1 = HRK 7.53450
- **hasMinorUnit**: 2
- **hasNumericCode**: 191
- **explanatoryNote**: The Kuna (HRK) will be retained in FIBO at least through 2023 due to the possibility of dual listing and to support instrument pricing that predated this change.
- **hasTextualName**: Kuna

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
