---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: approved reporting mechanism
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: data reporting services provider that is authorized to provide the service of reporting details of transactions
      to competent authorities or ESMA (the European Securities and Markets Authority) on behalf of investment firms
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ARM
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.esma.europa.eu/press-news/esma-news/esma-identifies-data-reporting-services-providers-be-supervised-directly
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lawinsider.com/dictionary/approved-reporting-mechanism
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-ARMS
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/DataReportingServicesProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DataReportingServicesProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ApprovedReportingMechanism
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: approved reporting mechanism
type: Ontology Class
---

# approved reporting mechanism

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ApprovedReportingMechanism>

## Definition

data reporting services provider that is authorized to provide the service of reporting details of transactions to competent authorities or ESMA (the European Securities and Markets Authority) on behalf of investment firms

## Relationships

- **Subclass of**: [DataReportingServicesProvider](/concepts/fibo/FBC/FunctionalEntities/Markets/DataReportingServicesProvider.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-ARMS`

## Annotations

- **label**: approved reporting mechanism
- **definition**: data reporting services provider that is authorized to provide the service of reporting details of transactions to competent authorities or ESMA (the European Securities and Markets Authority) on behalf of investment firms
- **abbreviation**: ARM
- **adaptedFrom**: https://www.esma.europa.eu/press-news/esma-news/esma-identifies-data-reporting-services-providers-be-supervised-directly
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **adaptedFrom**: https://www.lawinsider.com/dictionary/approved-reporting-mechanism

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
