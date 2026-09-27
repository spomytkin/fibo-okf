---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: institutional person
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: person that resides in an institution for some reason, due, for example, to hospitalization, rehabilitation, or
      incarceration
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalPerson
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: institutional person
type: Ontology Class
---

# institutional person

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalPerson>

## Definition

person that resides in an institution for some reason, due, for example, to hospitalization, rehabilitation, or incarceration

## Relationships

- **Subclass of**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)

## Annotations

- **label**: institutional person
- **definition**: person that resides in an institution for some reason, due, for example, to hospitalization, rehabilitation, or incarceration
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
