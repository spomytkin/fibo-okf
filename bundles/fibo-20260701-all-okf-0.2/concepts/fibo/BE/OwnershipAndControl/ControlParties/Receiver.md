---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: receiver
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party appointed by some court for the purposes of winding up the affairs of some entity which is no longer solvent
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/CourtAppointedControl
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControllingPartyIn
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/Receiver
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: receiver
type: Ontology Class
---

# receiver

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/Receiver>

## Definition

party appointed by some court for the purposes of winding up the affairs of some entity which is no longer solvent

## Relationships

- **Subclass of**: [DeJureControllingInterestParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)

## Constraints

- **[isControllingPartyIn](/concepts/fibo/FND/OwnershipAndControl/Control/isControllingPartyIn.md)**: some values from of type [CourtAppointedControl](/concepts/fibo/BE/OwnershipAndControl/ControlParties/CourtAppointedControl.md)

## Annotations

- **label**: receiver
- **definition**: party appointed by some court for the purposes of winding up the affairs of some entity which is no longer solvent

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
