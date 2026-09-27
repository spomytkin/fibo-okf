---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: alternative trading system
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trading venue that is more loosely regulated than a regulated exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ATS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The SEC formally defines an alternative trading system as any organization, association, person, group of persons,
      or systems (1) that constitutes, maintains, or provides a market place or facilities for bringing together purchasers
      and sellers of securities or for otherwise performing with respect to securities the functions commonly performed by
      a stock exchange within the meaning of Rule 3b-16 under the Exchange Act; and (2) that does not (i) set rules governing
      the conduct of subscribers other than the conduct of such subscribers' trading on such organization, association, person,
      group of persons, or system, or (ii) discipline subscribers other than by exclusion from trading.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-ATSS
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: alternative trading system
type: Ontology Class
---

# alternative trading system

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem>

## Definition

trading venue that is more loosely regulated than a regulated exchange

## Relationships

- **Subclass of**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-ATSS`

## Annotations

- **label**: alternative trading system
- **definition**: trading venue that is more loosely regulated than a regulated exchange
- **abbreviation**: ATS
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **explanatoryNote**: The SEC formally defines an alternative trading system as any organization, association, person, group of persons, or systems (1) that constitutes, maintains, or provides a market place or facilities for bringing together purchasers and sellers of securities or for otherwise performing with respect to securities the functions commonly performed by a stock exchange within the meaning of Rule 3b-16 under the Exchange Act; and (2) that does not (i) set rules governing the conduct of subscribers other than the conduct of such subscribers' trading on such organization, association, person, group of persons, or system, or (ii) discipline subscribers other than by exclusion from trading.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
