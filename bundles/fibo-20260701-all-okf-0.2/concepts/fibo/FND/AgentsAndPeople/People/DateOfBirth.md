---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: date of birth
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: explicit date, i.e., the day, month and year, on which an individual was born
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: birth date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: birthday
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfBirth
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: date of birth
type: Ontology Class
---

# date of birth

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfBirth>

## Definition

explicit date, i.e., the day, month and year, on which an individual was born

## Relationships

- **Subclass of**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)

## Annotations

- **label**: date of birth
- **definition**: explicit date, i.e., the day, month and year, on which an individual was born
- **synonym**: birth date
- **synonym**: birthday

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
