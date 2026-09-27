---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: religious corporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: not-for-profit corporation whose objective is specific to some fundamental set of beliefs and practices generally
      agreed upon by a number of people, and that is incorporated under the law
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Often religious corporations are recognized under the law on a sub-national level, for instance by a state or provincial
      government. The government agency responsible for regulating such corporations is usually the official holder of records,
      for instance a state department of corporations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/ReligiousObjective
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/NotForProfitCorporation
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ReligiousCorporation
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: religious corporation
type: Ontology Class
---

# religious corporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ReligiousCorporation>

## Definition

not-for-profit corporation whose objective is specific to some fundamental set of beliefs and practices generally agreed upon by a number of people, and that is incorporated under the law

## Relationships

- **Subclass of**: [NotForProfitCorporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: some values from of type [ReligiousObjective](/concepts/fibo/BE/LegalEntities/LegalPersons/ReligiousObjective.md)

## Annotations

- **label**: religious corporation
- **definition**: not-for-profit corporation whose objective is specific to some fundamental set of beliefs and practices generally agreed upon by a number of people, and that is incorporated under the law
- **explanatoryNote**: Often religious corporations are recognized under the law on a sub-national level, for instance by a state or provincial government. The government agency responsible for regulating such corporations is usually the official holder of records, for instance a state department of corporations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
