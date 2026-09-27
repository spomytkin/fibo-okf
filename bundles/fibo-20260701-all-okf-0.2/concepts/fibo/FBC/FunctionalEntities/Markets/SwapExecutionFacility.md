---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap execution facility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exchange that enables participants to execute and trade swaps
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SEF
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Swap execution facilities, including trading systems and other platforms, allow for greater transparency and represent
      a significant shift in the way derivative trading has been done. The Dodd-Frank Act lays the foundation for this change
      of derivative execution.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-SEFS
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SwapExecutionFacility
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: swap execution facility
type: Ontology Class
---

# swap execution facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SwapExecutionFacility>

## Definition

exchange that enables participants to execute and trade swaps

## Relationships

- **Subclass of**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-SEFS`

## Annotations

- **label**: swap execution facility
- **definition**: exchange that enables participants to execute and trade swaps
- **abbreviation**: SEF
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **explanatoryNote**: Swap execution facilities, including trading systems and other platforms, allow for greater transparency and represent a significant shift in the way derivative trading has been done. The Dodd-Frank Act lays the foundation for this change of derivative execution.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
