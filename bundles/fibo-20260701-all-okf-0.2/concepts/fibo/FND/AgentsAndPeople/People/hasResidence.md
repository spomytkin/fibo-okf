---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has residence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a dwelling where an individual lives
  domain:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Places/Addresses/hasAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasResidence
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has residence
type: Ontology Property
---

# has residence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasResidence>

## Definition

identifies a dwelling where an individual lives

## Relationships

- **Domain**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **Range**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **Subproperty of**: [hasAddress](/concepts/fibo/FND/Places/Addresses/hasAddress.md)

## Annotations

- **label**: has residence
- **definition**: identifies a dwelling where an individual lives

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
