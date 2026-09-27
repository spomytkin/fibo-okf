---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: party role identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters, capable of uniquely identifying a party based on a specific role that they play in some
      context
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentifier
sources:
- id: fibo-source-2c7ef9cc41
  resource: references/fibo/FND/Parties/Parties.rdf
  sha256: 2c7ef9cc4107e85b5bba3894094e496bcf4e8fe3ef9d6ce3b7d0830fb284f61d
  title: FIBO source FND/Parties/Parties.rdf
title: party role identifier
type: Ontology Class
---

# party role identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentifier>

## Definition

sequence of characters, capable of uniquely identifying a party based on a specific role that they play in some context

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: exact qualified cardinality 1 of type [PartyRoleIdentificationScheme](/concepts/fibo/FND/Parties/Parties/PartyRoleIdentificationScheme.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [PartyRoleIdentificationScheme](/concepts/fibo/FND/Parties/Parties/PartyRoleIdentificationScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label**: party role identifier
- **definition**: sequence of characters, capable of uniquely identifying a party based on a specific role that they play in some context

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
