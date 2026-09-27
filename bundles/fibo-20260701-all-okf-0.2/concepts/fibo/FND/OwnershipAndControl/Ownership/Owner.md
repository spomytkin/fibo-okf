---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: owner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that is legally recognized as having the right to possess, the privilege to use, and ability to transfer
      any rights or privileges associated with something, as permitted by law
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isOwningParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/ownsAsset
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Actor
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: owner
type: Ontology Class
---

# owner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner>

## Definition

party that is legally recognized as having the right to possess, the privilege to use, and ability to transfer any rights or privileges associated with something, as permitted by law

## Relationships

- **Subclass of**: [Actor](<https://www.omg.org/spec/Commons/PartiesAndSituations/Actor>)

## Constraints

- **[isOwningParty](/concepts/fibo/FND/OwnershipAndControl/Ownership/isOwningParty.md)**: some values from of type [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)
- **[ownsAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/ownsAsset.md)**: some values from of type [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Annotations

- **label**: owner
- **definition**: party that is legally recognized as having the right to possess, the privilege to use, and ability to transfer any rights or privileges associated with something, as permitted by law

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
