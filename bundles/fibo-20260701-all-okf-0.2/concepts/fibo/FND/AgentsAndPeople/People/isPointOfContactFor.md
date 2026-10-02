---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is point of contact for
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: is the entity or purpose for which the party is the point of contact
  domain:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Contact.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Contact
  inverse_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/hasPointOfContact.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPointOfContact
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/hasRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/isPointOfContactFor
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: is point of contact for
type: Ontology Property
---

# is point of contact for

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/isPointOfContactFor>

## Definition

is the entity or purpose for which the party is the point of contact

## Relationships

- **Domain**: [Contact](/concepts/fibo/FND/AgentsAndPeople/People/Contact.md)
- **Inverse of**: [hasPointOfContact](/concepts/fibo/FND/AgentsAndPeople/People/hasPointOfContact.md)
- **Subproperty of**: [hasRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/hasRole>)

## Annotations

- **label**: is point of contact for
- **definition**: is the entity or purpose for which the party is the point of contact

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
