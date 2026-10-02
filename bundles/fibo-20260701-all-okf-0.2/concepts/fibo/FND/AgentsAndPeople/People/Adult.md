---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: adult
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: person who has attained the age of majority as defined in some jurisdiction
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Adult
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/AgeOfMajority
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasAgeOfMajority
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Adult
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: adult
type: Ontology Class
---

# adult

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Adult>

## Definition

person who has attained the age of majority as defined in some jurisdiction

## Relationships

- **Subclass of**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)

## Constraints

- **[hasAgeOfMajority](/concepts/fibo/FND/AgentsAndPeople/People/hasAgeOfMajority.md)**: min qualified cardinality 0 of type [AgeOfMajority](/concepts/fibo/FND/AgentsAndPeople/People/AgeOfMajority.md)

## Annotations

- **label**: adult
- **definition**: person who has attained the age of majority as defined in some jurisdiction
- **adaptedFrom**: https://en.wikipedia.org/wiki/Adult

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
