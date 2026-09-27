---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: minor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a person under a certain age, usually the age of majority in a given jurisdiction, which legally demarcates childhood
      from adulthood
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Minor_(law)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The age depends upon jurisdiction and application, but is generally 18.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Minor
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: minor
type: Ontology Class
---

# minor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Minor>

## Definition

a person under a certain age, usually the age of majority in a given jurisdiction, which legally demarcates childhood from adulthood

## Relationships

- **Subclass of**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)

## Annotations

- **label**: minor
- **definition**: a person under a certain age, usually the age of majority in a given jurisdiction, which legally demarcates childhood from adulthood
- **adaptedFrom**: https://en.wikipedia.org/wiki/Minor_(law)
- **explanatoryNote**: The age depends upon jurisdiction and application, but is generally 18.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
