---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has date of death
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the date on which an individual died
  characteristics:
  - functional
  domain:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
  range:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/DateOfDeath.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfDeath
  rdf_types:
  - http://www.w3.org/2002/07/owl#FunctionalProperty
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasDateOfDeath
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has date of death
type: Ontology Property
---

# has date of death

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasDateOfDeath>

## Definition

identifies the date on which an individual died

## Relationships

- **Domain**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **Range**: [DateOfDeath](/concepts/fibo/FND/AgentsAndPeople/People/DateOfDeath.md)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has date of death
- **definition**: identifies the date on which an individual died

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
