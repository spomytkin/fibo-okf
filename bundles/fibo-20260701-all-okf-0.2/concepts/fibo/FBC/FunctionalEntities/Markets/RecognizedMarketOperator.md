---
owl:
  annotations:
  - language: en-GB
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: recognised market operator
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: recognized market operator
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exchange that is operated or maintained by an operator registered under certain securities regulations that brings
      together purchasers and sellers of capital market products
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: RMO
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.igi-global.com/dictionary/regulating-fintech-businesses/77383
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lawinsider.com/dictionary/recognized-market
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.mas.gov.sg/regulation/capital-markets/approved-exchange-ae-or-recognised-market-operator-rmo-licence
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-RMOS
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RecognizedMarketOperator
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: recognised market operator
type: Ontology Class
---

# recognised market operator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RecognizedMarketOperator>

## Definition

exchange that is operated or maintained by an operator registered under certain securities regulations that brings together purchasers and sellers of capital market products

## Relationships

- **Subclass of**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-RMOS`

## Annotations

- **label** (en-GB): recognised market operator
- **label** (en-US): recognized market operator
- **definition**: exchange that is operated or maintained by an operator registered under certain securities regulations that brings together purchasers and sellers of capital market products
- **abbreviation**: RMO
- **adaptedFrom**: https://www.igi-global.com/dictionary/regulating-fintech-businesses/77383
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **adaptedFrom**: https://www.lawinsider.com/dictionary/recognized-market
- **adaptedFrom**: https://www.mas.gov.sg/regulation/capital-markets/approved-exchange-ae-or-recognised-market-operator-rmo-licence

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
