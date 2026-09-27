---
owl:
  annotations:
  - language: en-GB
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: programme identifier
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: program identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters uniquely identifying a specific program within the context in which that program is administered
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Program
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/ContextualIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/ProgramIdentifier
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: program identifier
type: Ontology Class
---

# program identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/ProgramIdentifier>

## Definition

sequence of characters uniquely identifying a specific program within the context in which that program is administered

## Relationships

- **Subclass of**: [ContextualIdentifier](<https://www.omg.org/spec/Commons/ContextualIdentifiers/ContextualIdentifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [Program](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Program.md)

## Annotations

- **label** (en-GB): programme identifier
- **label** (en-US): program identifier
- **definition**: sequence of characters uniquely identifying a specific program within the context in which that program is administered

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
