---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: institutional unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that is capable, in its own right, of owning assets, incurring liabilities, and engaging in economic activities
      and in transactions with other parties
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=1415
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/eng/concepts/units
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.statcan.gc.ca/en/concepts/ccius/intro
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There is a hierarchical relationship between institutional units and establishments. An institutional unit contains
      one or more entire establishment(s); an establishment belongs to one and only one institutional unit. There are two
      main types of units in the real world that may qualify as institutional units, namely persons or groups of persons in
      the form of households, and legal or social entities.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: institutional unit
type: Ontology Class
---

# institutional unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit>

## Definition

party that is capable, in its own right, of owning assets, incurring liabilities, and engaging in economic activities and in transactions with other parties

## Relationships

- **Subclass of**: [FunctionalEntity](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md)
- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label**: institutional unit
- **definition**: party that is capable, in its own right, of owning assets, incurring liabilities, and engaging in economic activities and in transactions with other parties
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=1415
- **adaptedFrom**: http://www.statcan.gc.ca/eng/concepts/units
- **adaptedFrom**: https://www.statcan.gc.ca/en/concepts/ccius/intro
- **explanatoryNote**: There is a hierarchical relationship between institutional units and establishments. An institutional unit contains one or more entire establishment(s); an establishment belongs to one and only one institutional unit. There are two main types of units in the real world that may qualify as institutional units, namely persons or groups of persons in the form of households, and legal or social entities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
