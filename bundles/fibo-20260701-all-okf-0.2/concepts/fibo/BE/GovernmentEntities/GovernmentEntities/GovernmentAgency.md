---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government agency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: permanent or semi-permanent organization, often an appointed commission, in the machinery of government that is
      responsible for the oversight and administration of specific functions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There is a notable variety of agency types. Although usage differs, a government agency is normally distinct both
      from a department or ministry, and other types of public body established by government. The functions of an agency
      are normally executive in character, since different types of organizations (such as commissions) are most often constituted
      in an advisory role; this distinction is often blurred in practice however.
  disjoint_with:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentDepartment.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentDepartment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAppointee
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAgency
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: government agency
type: Ontology Class
---

# government agency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAgency>

## Definition

permanent or semi-permanent organization, often an appointed commission, in the machinery of government that is responsible for the oversight and administration of specific functions

## Relationships

- **Subclass of**: [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)

## Constraints

- **Disjoint with**: [GovernmentDepartment](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentDepartment.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: min qualified cardinality 0 of type [GovernmentAppointee](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentAppointee.md)

## Annotations

- **label**: government agency
- **definition**: permanent or semi-permanent organization, often an appointed commission, in the machinery of government that is responsible for the oversight and administration of specific functions
- **explanatoryNote**: There is a notable variety of agency types. Although usage differs, a government agency is normally distinct both from a department or ministry, and other types of public body established by government. The functions of an agency are normally executive in character, since different types of organizations (such as commissions) are most often constituted in an advisory role; this distinction is often blurred in practice however.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
