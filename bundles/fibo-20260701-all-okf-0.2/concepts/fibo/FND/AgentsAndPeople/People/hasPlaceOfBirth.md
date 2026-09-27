---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has place of birth
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the location where an individual was born
  domain:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
  range:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/PlaceOfBirth.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PlaceOfBirth
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPlaceOfBirth
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has place of birth
type: Ontology Property
---

# has place of birth

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPlaceOfBirth>

## Definition

identifies the location where an individual was born

## Relationships

- **Domain**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **Range**: [PlaceOfBirth](/concepts/fibo/FND/AgentsAndPeople/People/PlaceOfBirth.md)
- **Subproperty of**: [isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)

## Annotations

- **label**: has place of birth
- **definition**: identifies the location where an individual was born

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
