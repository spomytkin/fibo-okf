---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contact
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: role or associated with a party serving as a designated point of communication, typically within a system or process
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/ContactRecord
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isSignifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Contact
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: contact
type: Ontology Class
---

# contact

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Contact>

## Definition

role or associated with a party serving as a designated point of communication, typically within a system or process

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[isSignifiedBy](<https://www.omg.org/spec/Commons/Designators/isSignifiedBy>)**: some values from of type [ContactRecord](/concepts/fibo/FND/AgentsAndPeople/People/ContactRecord.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: some values from of type [PartyRoleIdentifier](/concepts/fibo/FND/Parties/Parties/PartyRoleIdentifier.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)

## Annotations

- **label**: contact
- **definition**: role or associated with a party serving as a designated point of communication, typically within a system or process

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
