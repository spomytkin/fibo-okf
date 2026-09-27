---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has owning party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the actor that holds title to the asset in an ownership situation
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
  inverse_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/isOwningParty.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isOwningParty
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwningParty
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: has owning party
type: Ontology Property
---

# has owning party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwningParty>

## Definition

identifies the actor that holds title to the asset in an ownership situation

## Relationships

- **Domain**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)
- **Inverse of**: [isOwningParty](/concepts/fibo/FND/OwnershipAndControl/Ownership/isOwningParty.md)
- **Range**: [Owner](/concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md)
- **Subproperty of**: [hasActor](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor>)

## Annotations

- **label**: has owning party
- **definition**: identifies the actor that holds title to the asset in an ownership situation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
