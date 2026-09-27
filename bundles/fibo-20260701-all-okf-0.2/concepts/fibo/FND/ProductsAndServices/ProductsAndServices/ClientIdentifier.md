---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: client identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters uniquely identifying a client within the context of some organization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Client
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - concept: /concepts/fibo/FND/Parties/Parties/PartyRoleIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ClientIdentifier
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: client identifier
type: Ontology Class
---

# client identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ClientIdentifier>

## Definition

sequence of characters uniquely identifying a client within the context of some organization

## Relationships

- **Subclass of**: [PartyRoleIdentifier](/concepts/fibo/FND/Parties/Parties/PartyRoleIdentifier.md)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Client](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Client.md)

## Annotations

- **label**: client identifier
- **definition**: sequence of characters uniquely identifying a client within the context of some organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
