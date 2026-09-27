---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entity that is formed and administered as per commercial law in order to engage in business activities
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are many types of business entities defined in the legal systems of various countries. These include corporations,
      cooperatives, partnerships, sole proprietorships, sole traders, limited liability companies, certain trusts and trust
      companies, and so forth. The rules vary by country and by state or province. Some of the more widely recognized types
      in the US, UK, and EU are defined in FIBO, by region. However, the regulations governing particular types of entity,
      even those described as roughly equivalent, differ from jurisdiction to jurisdiction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/BusinessObjective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/License
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: business entity
type: Ontology Class
---

# business entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity>

## Definition

entity that is formed and administered as per commercial law in order to engage in business activities

## Relationships

- **Subclass of**: [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [BusinessObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessObjective.md)
- **[holds](/concepts/fibo/FND/Relations/Relations/holds.md)**: min qualified cardinality 0 of type [License](/concepts/fibo/FND/Law/LegalCapacity/License.md)

## Annotations

- **label**: business entity
- **definition**: entity that is formed and administered as per commercial law in order to engage in business activities
- **explanatoryNote**: There are many types of business entities defined in the legal systems of various countries. These include corporations, cooperatives, partnerships, sole proprietorships, sole traders, limited liability companies, certain trusts and trust companies, and so forth. The rules vary by country and by state or province. Some of the more widely recognized types in the US, UK, and EU are defined in FIBO, by region. However, the regulations governing particular types of entity, even those described as roughly equivalent, differ from jurisdiction to jurisdiction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
