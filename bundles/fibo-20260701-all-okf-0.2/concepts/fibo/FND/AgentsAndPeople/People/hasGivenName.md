---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has given name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the given name or first name of a person, that is, the name chosen for them at birth or changed by them
      subsequently from the name given at birth
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/hasPersonName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPersonName
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasGivenName
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has given name
type: Ontology Property
---

# has given name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasGivenName>

## Definition

indicates the given name or first name of a person, that is, the name chosen for them at birth or changed by them subsequently from the name given at birth

## Relationships

- **Subproperty of**: [hasPersonName](/concepts/fibo/FND/AgentsAndPeople/People/hasPersonName.md)

## Annotations

- **label**: has given name
- **definition**: indicates the given name or first name of a person, that is, the name chosen for them at birth or changed by them subsequently from the name given at birth

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
