---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: project name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contextual designation for a project
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Project
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isNameOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/ContextualName
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/ProjectName
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: project name
type: Ontology Class
---

# project name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/ProjectName>

## Definition

contextual designation for a project

## Relationships

- **Subclass of**: [ContextualName](<https://www.omg.org/spec/Commons/ContextualDesignators/ContextualName>)

## Constraints

- **[isNameOf](<https://www.omg.org/spec/Commons/Designators/isNameOf>)**: some values from of type [Project](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Project.md)

## Annotations

- **label**: project name
- **definition**: contextual designation for a project

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
