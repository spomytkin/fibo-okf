---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: influence-based de facto controlling party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that holds influence-based control over some other party
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Regulatory or jurisdictional control would fall under this control. Court appointed control is de jure control
      BUT the scenario in which a government takes over something and then hands it over to some new de jure controller i.e.
      administrator - in the meantime this is de facto control by e.g. the government.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InfluenceBasedDeFactoControl
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControllingPartyIn
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InfluenceBasedDeFactoControllingParty
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: influence-based de facto controlling party
type: Ontology Class
---

# influence-based de facto controlling party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InfluenceBasedDeFactoControllingParty>

## Definition

party that holds influence-based control over some other party

## Relationships

- **Subclass of**: [DeFactoControllingInterestParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty.md)

## Constraints

- **[isControllingPartyIn](/concepts/fibo/FND/OwnershipAndControl/Control/isControllingPartyIn.md)**: some values from of type [InfluenceBasedDeFactoControl](/concepts/fibo/BE/OwnershipAndControl/ControlParties/InfluenceBasedDeFactoControl.md)

## Annotations

- **label**: influence-based de facto controlling party
- **definition**: party that holds influence-based control over some other party
- **editorialNote**: Regulatory or jurisdictional control would fall under this control. Court appointed control is de jure control BUT the scenario in which a government takes over something and then hands it over to some new de jure controller i.e. administrator - in the meantime this is de facto control by e.g. the government.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
