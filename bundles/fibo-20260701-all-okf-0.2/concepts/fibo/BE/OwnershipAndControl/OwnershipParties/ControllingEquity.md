---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: controlling equity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: shareholders's equity that formally confers control in the entity, either by law or as explicitly stated in a corresponding
      equity instrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeJureControl
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/ShareholdersEquity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/ShareholdersEquity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ControllingEquity
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: controlling equity
type: Ontology Class
---

# controlling equity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ControllingEquity>

## Definition

shareholders's equity that formally confers control in the entity, either by law or as explicitly stated in a corresponding equity instrument

## Relationships

- **Subclass of**: [ShareholdersEquity](/concepts/fibo/FND/OwnershipAndControl/Ownership/ShareholdersEquity.md)

## Constraints

- **[confers](/concepts/fibo/FND/Relations/Relations/confers.md)**: all values from of type [DeJureControl](/concepts/fibo/FND/OwnershipAndControl/Control/DeJureControl.md)

## Annotations

- **label**: controlling equity
- **definition**: shareholders's equity that formally confers control in the entity, either by law or as explicitly stated in a corresponding equity instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
