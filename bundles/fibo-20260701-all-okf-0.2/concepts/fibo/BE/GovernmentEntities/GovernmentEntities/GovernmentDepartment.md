---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government department
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specialized organization responsible for a sector of government public administration
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentMinister
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentDepartment
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: government department
type: Ontology Class
---

# government department

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentDepartment>

## Definition

specialized organization responsible for a sector of government public administration

## Relationships

- **Subclass of**: [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)

## Constraints

- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: min qualified cardinality 0 of type [GovernmentMinister](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentMinister.md)

## Annotations

- **label**: government department
- **definition**: specialized organization responsible for a sector of government public administration

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
