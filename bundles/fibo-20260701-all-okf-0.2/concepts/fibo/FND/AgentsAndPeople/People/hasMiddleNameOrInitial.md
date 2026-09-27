---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has middle name or initial
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: one or more additional names or initial letters for names that occur between a person's first and last name
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/hasPersonName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPersonName
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasMiddleNameOrInitial
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has middle name or initial
type: Ontology Property
---

# has middle name or initial

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasMiddleNameOrInitial>

## Definition

one or more additional names or initial letters for names that occur between a person's first and last name

## Relationships

- **Subproperty of**: [hasPersonName](/concepts/fibo/FND/AgentsAndPeople/People/hasPersonName.md)

## Annotations

- **label**: has middle name or initial
- **definition**: one or more additional names or initial letters for names that occur between a person's first and last name

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
