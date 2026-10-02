---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: civilian non-institutional population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical universe consisting of people of a certain age who reside in a given region, do not live in institutions
      (for example, correctional facilities, long-term care hospitals, and nursing homes), and are not on active military
      duty
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: The civilian non-institutional population is typically reported in thousands.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPerson
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalUniverse
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: civilian non-institutional population
type: Ontology Class
---

# civilian non-institutional population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation>

## Definition

statistical universe consisting of people of a certain age who reside in a given region, do not live in institutions (for example, correctional facilities, long-term care hospitals, and nursing homes), and are not on active military duty

## Relationships

- **Subclass of**: [StatisticalUniverse](/concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [CivilianNonInstitutionalPerson](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPerson.md)

## Annotations

- **label**: civilian non-institutional population
- **definition**: statistical universe consisting of people of a certain age who reside in a given region, do not live in institutions (for example, correctional facilities, long-term care hospitals, and nursing homes), and are not on active military duty
- **scopeNote**: The civilian non-institutional population is typically reported in thousands.
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
