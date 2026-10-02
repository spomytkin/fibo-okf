---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NOK-NIBOR-NIBR-Reference Banks
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: http://www.w3.org/2002/07/owl#deprecated
    value: 'true'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: NOK-NIBOR-NIBR-Reference Banks
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Deprecated usage: NOK-NIBOR-NIBR-Reference Banks. It was added to FpML in error, NOK-NIBOR-Reference Banks should
      be used instead.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented
      through the date on which parties enter into the relevant transaction.
  deprecated: true
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/NorwegianKrone.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/NorwegianKrone
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/NOK-NIBOR-NIBR-Reference_Banks
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: NOK-NIBOR-NIBR-Reference Banks
type: Ontology Individual
---

# NOK-NIBOR-NIBR-Reference Banks

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/NOK-NIBOR-NIBR-Reference_Banks>

## Relationships

- **Related to**: [NorwegianKrone](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/NorwegianKrone.md)

## Annotations

- **label**: NOK-NIBOR-NIBR-Reference Banks
- **deprecated**: true
- **abbreviation**: NOK-NIBOR-NIBR-Reference Banks
- **explanatoryNote**: Deprecated usage: NOK-NIBOR-NIBR-Reference Banks. It was added to FpML in error, NOK-NIBOR-Reference Banks should be used instead.
- **explanatoryNote**: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
