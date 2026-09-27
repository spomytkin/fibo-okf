---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tribal government
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: government representing a group of indigenous people that has legal authority to govern those people, including
      authority to legislate the existence of tribal entities
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/TribalArea
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/TribalGovernment
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: tribal government
type: Ontology Class
---

# tribal government

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/TribalGovernment>

## Definition

government representing a group of indigenous people that has legal authority to govern those people, including authority to legislate the existence of tribal entities

## Relationships

- **Subclass of**: [Government](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md)

## Constraints

- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [TribalArea](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/TribalArea.md)

## Annotations

- **label**: tribal government
- **definition**: government representing a group of indigenous people that has legal authority to govern those people, including authority to legislate the existence of tribal entities

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
