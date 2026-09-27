---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: military person
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: person that is a member of the active duty military
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Civilian.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Civilian
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/MilitaryPerson
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: military person
type: Ontology Class
---

# military person

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/MilitaryPerson>

## Definition

person that is a member of the active duty military

## Relationships

- **Subclass of**: [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)

## Constraints

- **Disjoint with**: [Civilian](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Civilian.md)

## Annotations

- **label**: military person
- **definition**: person that is a member of the active duty military
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
