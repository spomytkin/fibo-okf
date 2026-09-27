---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: HKD-Quarterly-Annual Swap Rate-Reference Banks
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: http://www.w3.org/2002/07/owl#deprecated
    value: 'true'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: HKD-Quarterly-Annual Swap Rate-Reference Banks
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Deprecated usage: "HKD-Quarterly-Annual Swap Rate-Reference Banks" code has been deprecated in supplement 79 to
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
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/HKD-Quarterly-Annual_Swap_Rate-Reference_Banks
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: HKD-Quarterly-Annual Swap Rate-Reference Banks
type: Ontology Individual
---

# HKD-Quarterly-Annual Swap Rate-Reference Banks

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/HKD-Quarterly-Annual_Swap_Rate-Reference_Banks>

## Relationships

- **Related to**: [HongKongDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/HongKongDollar.md)
- **Related to**: [ThreeMonths](/concepts/fibo/IND/InterestRates/InterestRates/ThreeMonths.md)

## Annotations

- **label**: HKD-Quarterly-Annual Swap Rate-Reference Banks
- **deprecated**: true
- **abbreviation**: HKD-Quarterly-Annual Swap Rate-Reference Banks
- **explanatoryNote**: Deprecated usage: "HKD-Quarterly-Annual Swap Rate-Reference Banks" code has been deprecated in supplement 79 to the 2006 ISDA definitions (Removal of certain Hong Kong Rate Options.). The code is kept in FpML for backward compatibility purposes.
- **explanatoryNote**: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
