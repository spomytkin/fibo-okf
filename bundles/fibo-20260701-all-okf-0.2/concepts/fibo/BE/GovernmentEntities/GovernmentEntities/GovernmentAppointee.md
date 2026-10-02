---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government appointee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual designated by government decree to lead, or participate in some capacity in a government body
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentOfficial.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentOfficial
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Executive.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Executive
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAppointee
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: government appointee
type: Ontology Class
---

# government appointee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAppointee>

## Definition

individual designated by government decree to lead, or participate in some capacity in a government body

## Relationships

- **Subclass of**: [GovernmentOfficial](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentOfficial.md)
- **Subclass of**: [Executive](/concepts/fibo/BE/OwnershipAndControl/Executives/Executive.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: min qualified cardinality 0

## Annotations

- **label**: government appointee
- **definition**: individual designated by government decree to lead, or participate in some capacity in a government body

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
