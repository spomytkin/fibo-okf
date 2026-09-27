---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is owned asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the context of ownership in which something is an asset
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/undergoes
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isOwnedAsset
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: is owned asset
type: Ontology Property
---

# is owned asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isOwnedAsset>

## Definition

indicates the context of ownership in which something is an asset

## Relationships

- **Domain**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **Range**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)
- **Subproperty of**: [undergoes](<https://www.omg.org/spec/Commons/PartiesAndSituations/undergoes>)

## Annotations

- **label**: is owned asset
- **definition**: indicates the context of ownership in which something is an asset

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
