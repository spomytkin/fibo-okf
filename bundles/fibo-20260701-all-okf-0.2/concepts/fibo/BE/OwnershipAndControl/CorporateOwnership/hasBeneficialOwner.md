---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has beneficial owner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the party that retains rights in the asset they own in a beneficial ownership situation
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/isAssetOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isAssetOf
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/hasBeneficialOwner
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
title: has beneficial owner
type: Ontology Property
---

# has beneficial owner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/hasBeneficialOwner>

## Definition

indicates the party that retains rights in the asset they own in a beneficial ownership situation

## Relationships

- **Domain**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **Range**: [BeneficialOwner](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md)
- **Subproperty of**: [isAssetOf](/concepts/fibo/FND/OwnershipAndControl/Ownership/isAssetOf.md)

## Annotations

- **label**: has beneficial owner
- **definition**: indicates the party that retains rights in the asset they own in a beneficial ownership situation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
