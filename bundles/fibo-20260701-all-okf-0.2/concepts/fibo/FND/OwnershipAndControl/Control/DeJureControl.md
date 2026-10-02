---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: de jure control
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: control that exists as a matter of law, i.e., legitimate, legal control of something
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalConstruct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalConstruct
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/Control.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeJureControl
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: de jure control
type: Ontology Class
---

# de jure control

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeJureControl>

## Definition

control that exists as a matter of law, i.e., legitimate, legal control of something

## Relationships

- **Subclass of**: [LegalConstruct](/concepts/fibo/FND/Law/LegalCapacity/LegalConstruct.md)
- **Subclass of**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)

## Annotations

- **label**: de jure control
- **definition**: control that exists as a matter of law, i.e., legitimate, legal control of something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
