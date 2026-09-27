---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market category classifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier representing the controlled vocabulary that delineates the nature of the exchange or data reporting
      services provider where possible
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: As of October 2022, the controlled vocabulary includes two codes that are not semantically useful, namely 'not
      specified', or NSPD, and 'other', or OTHR. These are included for the sake of completeness but ignored with respect
      to how the exchange or market is classified. If something has one of these two codes as a market category, they will
      be classified either as an operating-level or segment-level marketas appropriate with no other distinction in terms
      of how they are instantiated.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
    value: N040413530ced408db069b7c4d41c69d5
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ISO10383-ClassificationScheme
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: market category classifier
type: Ontology Class
---

# market category classifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier>

## Definition

classifier representing the controlled vocabulary that delineates the nature of the exchange or data reporting services provider where possible

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from value `N040413530ced408db069b7c4d41c69d5`
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ISO10383-ClassificationScheme`

## Annotations

- **label**: market category classifier
- **definition**: classifier representing the controlled vocabulary that delineates the nature of the exchange or data reporting services provider where possible
- **scopeNote**: As of October 2022, the controlled vocabulary includes two codes that are not semantically useful, namely 'not specified', or NSPD, and 'other', or OTHR. These are included for the sake of completeness but ignored with respect to how the exchange or market is classified. If something has one of these two codes as a market category, they will be classified either as an operating-level or segment-level marketas appropriate with no other distinction in terms of how they are instantiated.
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
