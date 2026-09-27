---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal working age person
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: person whose age is greater than the minimum legal working age specified in a jurisdiction in which they work
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/LegalWorkingAge
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasMinimumLegalWorkingAge
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/LegalWorkingAgePerson
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: legal working age person
type: Ontology Class
---

# legal working age person

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/LegalWorkingAgePerson>

## Definition

person whose age is greater than the minimum legal working age specified in a jurisdiction in which they work

## Relationships

- **Subclass of**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)

## Constraints

- **[hasMinimumLegalWorkingAge](/concepts/fibo/FND/AgentsAndPeople/People/hasMinimumLegalWorkingAge.md)**: min qualified cardinality 0 of type [LegalWorkingAge](/concepts/fibo/FND/AgentsAndPeople/People/LegalWorkingAge.md)

## Annotations

- **label**: legal working age person
- **definition**: person whose age is greater than the minimum legal working age specified in a jurisdiction in which they work

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
