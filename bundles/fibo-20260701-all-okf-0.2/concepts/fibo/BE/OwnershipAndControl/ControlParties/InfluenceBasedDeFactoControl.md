---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: influence-based de facto control
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: informal control that involves influence over some party
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InfluenceBasedDeFactoControllingParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasPartyInControl
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/DeFactoControl.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeFactoControl
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InfluenceBasedDeFactoControl
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: influence-based de facto control
type: Ontology Class
---

# influence-based de facto control

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InfluenceBasedDeFactoControl>

## Definition

informal control that involves influence over some party

## Relationships

- **Subclass of**: [DeFactoControl](/concepts/fibo/FND/OwnershipAndControl/Control/DeFactoControl.md)

## Constraints

- **[hasPartyInControl](/concepts/fibo/FND/OwnershipAndControl/Control/hasPartyInControl.md)**: some values from of type [InfluenceBasedDeFactoControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/InfluenceBasedDeFactoControllingParty.md)

## Annotations

- **label**: influence-based de facto control
- **definition**: informal control that involves influence over some party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
