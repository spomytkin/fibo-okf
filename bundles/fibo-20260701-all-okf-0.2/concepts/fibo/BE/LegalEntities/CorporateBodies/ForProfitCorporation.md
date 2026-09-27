---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: for profit corporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporation whose objective is to make money, i.e., to ensure realization of a financial benefit such that the
      amount of revenue gained from a business activity exceeds the expenses, costs and taxes needed to sustain that activity
  disjoint_with:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/NotForProfitCorporation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/ProfitObjective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ForProfitCorporation
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: for profit corporation
type: Ontology Class
---

# for profit corporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ForProfitCorporation>

## Definition

corporation whose objective is to make money, i.e., to ensure realization of a financial benefit such that the amount of revenue gained from a business activity exceeds the expenses, costs and taxes needed to sustain that activity

## Relationships

- **Subclass of**: [Corporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md)

## Constraints

- **Disjoint with**: [NotForProfitCorporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md)
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [ProfitObjective](/concepts/fibo/BE/LegalEntities/LegalPersons/ProfitObjective.md)

## Annotations

- **label**: for profit corporation
- **definition**: corporation whose objective is to make money, i.e., to ensure realization of a financial benefit such that the amount of revenue gained from a business activity exceeds the expenses, costs and taxes needed to sustain that activity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
