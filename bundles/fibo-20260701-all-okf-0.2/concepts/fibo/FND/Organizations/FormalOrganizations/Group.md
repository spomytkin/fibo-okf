---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: group
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection of agents (people, organizations, software agents, etc.) that are considered as a unit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Agent
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Group
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: group
type: Ontology Class
---

# group

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Group>

## Definition

collection of agents (people, organizations, software agents, etc.) that are considered as a unit

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: all values from of type [Agent](<https://www.omg.org/spec/Commons/PartiesAndSituations/Agent>)

## Annotations

- **label**: group
- **definition**: collection of agents (people, organizations, software agents, etc.) that are considered as a unit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
