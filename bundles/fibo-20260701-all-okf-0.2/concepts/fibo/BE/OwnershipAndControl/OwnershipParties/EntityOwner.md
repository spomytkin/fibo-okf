---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entity owner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: owner (person, group of people, or other business entity) that owns, or holds an ownership interest in, a formal
      business organization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/OwnersEquity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwner
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: entity owner
type: Ontology Class
---

# entity owner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwner>

## Definition

owner (person, group of people, or other business entity) that owns, or holds an ownership interest in, a formal business organization

## Relationships

- **Subclass of**: [Owner](/concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md)

## Constraints

- **[holds](/concepts/fibo/FND/Relations/Relations/holds.md)**: some values from of type [OwnersEquity](/concepts/fibo/FND/OwnershipAndControl/Ownership/OwnersEquity.md)

## Annotations

- **label**: entity owner
- **definition**: owner (person, group of people, or other business entity) that owns, or holds an ownership interest in, a formal business organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
