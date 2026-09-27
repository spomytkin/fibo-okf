---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: advises
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: provides counsel or guidance to
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/isAdvisedBy.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/isAdvisedBy
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/isPartyControlling.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isPartyControlling
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/advises
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: advises
type: Ontology Property
---

# advises

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/advises>

## Definition

provides counsel or guidance to

## Relationships

- **Domain**: [ControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md)
- **Inverse of**: [isAdvisedBy](/concepts/fibo/BE/OwnershipAndControl/ControlParties/isAdvisedBy.md)
- **Range**: [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **Subproperty of**: [isPartyControlling](/concepts/fibo/FND/OwnershipAndControl/Control/isPartyControlling.md)

## Annotations

- **label**: advises
- **definition**: provides counsel or guidance to

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
