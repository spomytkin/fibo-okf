---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has owned asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the asset in an ownership situation
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
  inverse_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/isOwnedAsset.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isOwnedAsset
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwnedAsset
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: has owned asset
type: Ontology Property
---

# has owned asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwnedAsset>

## Definition

indicates the asset in an ownership situation

## Relationships

- **Domain**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)
- **Inverse of**: [isOwnedAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/isOwnedAsset.md)
- **Range**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **Subproperty of**: [hasUndergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer>)

## Annotations

- **label**: has owned asset
- **definition**: indicates the asset in an ownership situation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
