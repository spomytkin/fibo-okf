---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: consolidated tape provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: data reporting services provider that is authorized to provide the service of collecting trade reports for financial
      instruments from regulated markets, MTFs, OTFs and APAs and consolidating them into a continuous electronic live data
      stream providing price and volume data per financial instrument
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CTP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.esma.europa.eu/press-news/esma-news/esma-identifies-data-reporting-services-providers-be-supervised-directly
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lawinsider.com/dictionary/consolidated-tape-providers-hereinafter-referred-to-as-ctp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Consolidated tape is an electronic system that collates real-time exchange-listed data, such as price and volume,
      and disseminates it to investors. Through the consolidated tape, various major exchanges, including the New York Stock
      Exchange, the NASDAQ, and the Chicago Board Options Exchange, report trades and quotes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-CTPS
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/DataReportingServicesProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DataReportingServicesProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ConsolidatedTapeProvider
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: consolidated tape provider
type: Ontology Class
---

# consolidated tape provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ConsolidatedTapeProvider>

## Definition

data reporting services provider that is authorized to provide the service of collecting trade reports for financial instruments from regulated markets, MTFs, OTFs and APAs and consolidating them into a continuous electronic live data stream providing price and volume data per financial instrument

## Relationships

- **Subclass of**: [DataReportingServicesProvider](/concepts/fibo/FBC/FunctionalEntities/Markets/DataReportingServicesProvider.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-CTPS`

## Annotations

- **label**: consolidated tape provider
- **definition**: data reporting services provider that is authorized to provide the service of collecting trade reports for financial instruments from regulated markets, MTFs, OTFs and APAs and consolidating them into a continuous electronic live data stream providing price and volume data per financial instrument
- **abbreviation**: CTP
- **adaptedFrom**: https://www.esma.europa.eu/press-news/esma-news/esma-identifies-data-reporting-services-providers-be-supervised-directly
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **adaptedFrom**: https://www.lawinsider.com/dictionary/consolidated-tape-providers-hereinafter-referred-to-as-ctp
- **explanatoryNote**: Consolidated tape is an electronic system that collates real-time exchange-listed data, such as price and volume, and disseminates it to investors. Through the consolidated tape, various major exchanges, including the New York Stock Exchange, the NASDAQ, and the Chicago Board Options Exchange, report trades and quotes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
