---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: not for profit objective
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: objective that reflects the charitable, educational, religious, humanitarian, public services, or other not for
      profit goals of an organization
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The objective of all business activities is not to earn profits for its owners. All of the money earned by or donated
      to a not for profit organization is used in pursuing the organization's objectives.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: nonprofit objective
  disjoint_with:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/ProfitObjective.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/ProfitObjective
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Objective.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Objective
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/NotForProfitObjective
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: not for profit objective
type: Ontology Class
---

# not for profit objective

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/NotForProfitObjective>

## Definition

objective that reflects the charitable, educational, religious, humanitarian, public services, or other not for profit goals of an organization

## Relationships

- **Subclass of**: [Objective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Objective.md)

## Constraints

- **Disjoint with**: [ProfitObjective](/concepts/fibo/BE/LegalEntities/LegalPersons/ProfitObjective.md)

## Annotations

- **label**: not for profit objective
- **definition**: objective that reflects the charitable, educational, religious, humanitarian, public services, or other not for profit goals of an organization
- **explanatoryNote**: The objective of all business activities is not to earn profits for its owners. All of the money earned by or donated to a not for profit organization is used in pursuing the organization's objectives.
- **synonym**: nonprofit objective

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
