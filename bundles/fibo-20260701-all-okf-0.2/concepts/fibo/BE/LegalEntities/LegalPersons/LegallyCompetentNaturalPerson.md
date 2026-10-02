---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legally competent natural person
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: person who is considered competent, under the circumstances, to enter into a contract, conduct business, or participate
      in other activities that generally require the mental ability to understand problems and make decisions on his or her
      own behalf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The definition of mental competence, and potentially of the age of majority, is a function of the situation and
      law in a given jurisdiction.
  disjoint_with:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/IncapacitatedAdult.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IncapacitatedAdult
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: legally competent natural person
type: Ontology Class
---

# legally competent natural person

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson>

## Definition

person who is considered competent, under the circumstances, to enter into a contract, conduct business, or participate in other activities that generally require the mental ability to understand problems and make decisions on his or her own behalf

## Relationships

- **Subclass of**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **Subclass of**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Constraints

- **Disjoint with**: [IncapacitatedAdult](/concepts/fibo/FND/AgentsAndPeople/People/IncapacitatedAdult.md)

## Annotations

- **label**: legally competent natural person
- **definition**: person who is considered competent, under the circumstances, to enter into a contract, conduct business, or participate in other activities that generally require the mental ability to understand problems and make decisions on his or her own behalf
- **explanatoryNote**: The definition of mental competence, and potentially of the age of majority, is a function of the situation and law in a given jurisdiction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
