---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has gender
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a particular gender value with a person
  characteristics:
  - functional
  domain:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  - http://www.w3.org/2002/07/owl#FunctionalProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasGender
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has gender
type: Ontology Property
---

# has gender

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasGender>

## Definition

links a particular gender value with a person

## Relationships

- **Domain**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: has gender
- **definition**: links a particular gender value with a person

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
