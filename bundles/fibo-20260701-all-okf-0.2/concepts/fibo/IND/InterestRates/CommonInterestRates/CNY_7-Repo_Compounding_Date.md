---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CNY 7-Repo Compounding Date
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: http://www.w3.org/2002/07/owl#deprecated
    value: 'true'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CNY 7-Repo Compounding Date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Deprecated usage: CNY 7-Repo Compounding Date - is not an floating rate index and should not be in the floating-rate-index
      list (it is a date).'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented
      through the date on which parties enter into the relevant transaction.
  deprecated: true
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/YuanRenminbi.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/YuanRenminbi
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/CNY_7-Repo_Compounding_Date
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: CNY 7-Repo Compounding Date
type: Ontology Individual
---

# CNY 7-Repo Compounding Date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/CNY_7-Repo_Compounding_Date>

## Relationships

- **Related to**: [YuanRenminbi](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/YuanRenminbi.md)

## Annotations

- **label**: CNY 7-Repo Compounding Date
- **deprecated**: true
- **abbreviation**: CNY 7-Repo Compounding Date
- **explanatoryNote**: Deprecated usage: CNY 7-Repo Compounding Date - is not an floating rate index and should not be in the floating-rate-index list (it is a date).
- **explanatoryNote**: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
