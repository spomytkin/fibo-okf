---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has point of contact
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a party designated as the point of contact for
  range:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Contact.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Contact
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/hasRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPointOfContact
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has point of contact
type: Ontology Property
---

# has point of contact

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPointOfContact>

## Definition

identifies a party designated as the point of contact for

## Relationships

- **Range**: [Contact](/concepts/fibo/FND/AgentsAndPeople/People/Contact.md)
- **Subproperty of**: [hasRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/hasRole>)

## Annotations

- **label**: has point of contact
- **definition**: identifies a party designated as the point of contact for

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
