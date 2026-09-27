---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: court appointed control
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: control conferred by the actions of some court, for example in the context of receivership
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/CourtOfLaw
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/DeJureControl.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeJureControl
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/CourtAppointedControl
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: court appointed control
type: Ontology Class
---

# court appointed control

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/CourtAppointedControl>

## Definition

control conferred by the actions of some court, for example in the context of receivership

## Relationships

- **Subclass of**: [DeJureControl](/concepts/fibo/FND/OwnershipAndControl/Control/DeJureControl.md)

## Constraints

- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: all values from of type [CourtOfLaw](/concepts/fibo/FND/Law/LegalCore/CourtOfLaw.md)

## Annotations

- **label**: court appointed control
- **definition**: control conferred by the actions of some court, for example in the context of receivership

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
