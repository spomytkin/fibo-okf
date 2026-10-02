---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: date of death
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: explicit date, i.e., the day, month and year, on which an individual died
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: death date
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfDeath
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: date of death
type: Ontology Class
---

# date of death

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfDeath>

## Definition

explicit date, i.e., the day, month and year, on which an individual died

## Relationships

- **Subclass of**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)

## Annotations

- **label**: date of death
- **definition**: explicit date, i.e., the day, month and year, on which an individual died
- **synonym**: death date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
