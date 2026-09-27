---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: INR-BMK
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: http://www.w3.org/2002/07/owl#deprecated
    value: 'true'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: INR-BMK
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Deprecated usage: "INR-BMK" code has been deprecated in supplement 54 to the 2006 ISDA definitions. The code is
      kept in FpML for backward compatibility purposes.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented
      through the date on which parties enter into the relevant transaction.
  deprecated: true
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/IndianRupee.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/IndianRupee
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/INR-BMK
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: INR-BMK
type: Ontology Individual
---

# INR-BMK

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/INR-BMK>

## Relationships

- **Related to**: [IndianRupee](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/IndianRupee.md)

## Annotations

- **label**: INR-BMK
- **deprecated**: true
- **abbreviation**: INR-BMK
- **explanatoryNote**: Deprecated usage: "INR-BMK" code has been deprecated in supplement 54 to the 2006 ISDA definitions. The code is kept in FpML for backward compatibility purposes.
- **explanatoryNote**: Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
