---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: elects
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: chooses someone, or a group of individuals, to hold office or some other position by voting
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: In the case of an election of the members of a board of directors, the bylaws state the manner in which that process
      is effected. The candidate members may be recommended by the board or other proxy and are then elected by the shareholders.
      A similar process may be conducted to elect outside auditors.
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: the election of officers of an association, the election of directors by the shareholders
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/elects
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: elects
type: Ontology Property
---

# elects

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/elects>

## Definition

chooses someone, or a group of individuals, to hold office or some other position by voting

## Relationships

- **Domain**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)
- **Range**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label**: elects
- **definition**: chooses someone, or a group of individuals, to hold office or some other position by voting
- **editorialNote**: In the case of an election of the members of a board of directors, the bylaws state the manner in which that process is effected. The candidate members may be recommended by the board or other proxy and are then elected by the shareholders. A similar process may be conducted to elect outside auditors.
- **example**: the election of officers of an association, the election of directors by the shareholders

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
