---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employed population temporarily not at work
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the employed population that includes persons that are temporarily absent from work for various reasons
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bls.gov/news.release/empsit.t15.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This includes persons temporarily not at work because of illness or injury, holiday or vacation, strike or lockout,
      educational or training leave, maternity or parental leave, reduction in economic activity, temporary disorganisation
      or suspension of work due to such reasons as bad weather, mechanical or electrical breakdown, or shortage of raw materials
      or fuels, or other temporary absence with or without leave should be considered as in paid employment provided they
      had a formal job attachment.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationTemporarilyNotAtWork
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: employed population temporarily not at work
type: Ontology Class
---

# employed population temporarily not at work

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationTemporarilyNotAtWork>

## Definition

subset of the employed population that includes persons that are temporarily absent from work for various reasons

## Relationships

- **Subclass of**: [EmployedPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md)

## Annotations

- **label**: employed population temporarily not at work
- **definition**: subset of the employed population that includes persons that are temporarily absent from work for various reasons
- **adaptedFrom**: https://www.bls.gov/news.release/empsit.t15.htm
- **explanatoryNote**: This includes persons temporarily not at work because of illness or injury, holiday or vacation, strike or lockout, educational or training leave, maternity or parental leave, reduction in economic activity, temporary disorganisation or suspension of work due to such reasons as bad weather, mechanical or electrical breakdown, or shortage of raw materials or fuels, or other temporary absence with or without leave should be considered as in paid employment provided they had a formal job attachment.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
