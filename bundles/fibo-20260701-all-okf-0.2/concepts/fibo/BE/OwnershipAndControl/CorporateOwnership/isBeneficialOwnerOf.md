---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is beneficial owner of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates an asset in which the beneficial owner holds rights (typically voting rights, management rights, etc.)
      in a beneficial ownership situation
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/hasBeneficialOwner.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/hasBeneficialOwner
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/ownsAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/ownsAsset
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/isBeneficialOwnerOf
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
title: is beneficial owner of
type: Ontology Property
---

# is beneficial owner of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/isBeneficialOwnerOf>

## Definition

indicates an asset in which the beneficial owner holds rights (typically voting rights, management rights, etc.) in a beneficial ownership situation

## Relationships

- **Domain**: [BeneficialOwner](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md)
- **Inverse of**: [hasBeneficialOwner](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/hasBeneficialOwner.md)
- **Range**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **Subproperty of**: [ownsAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/ownsAsset.md)

## Annotations

- **label**: is beneficial owner of
- **definition**: indicates an asset in which the beneficial owner holds rights (typically voting rights, management rights, etc.) in a beneficial ownership situation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
