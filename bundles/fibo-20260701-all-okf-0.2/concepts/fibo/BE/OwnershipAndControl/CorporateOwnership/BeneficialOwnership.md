---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: beneficial ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: situation linking party that enjoys the benefits of ownership (such as receipt of income) of something even though
      its ownership (title) may be in the name of another party (called a nominee or registered owner) to the asset that they
      own
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Beneficial ownership may be shared among a group of individuals. If a beneficial owner acquires a position of more
      than 5 percent in the United States, it must file Schedule 13D or 13G under Section 12 of the Securities Exchange Act
      of 1934.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwnedAsset
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwningParty
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: N6ec9848fcf5a4a45801e2f3248a9aa90
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwnership
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
title: beneficial ownership
type: Ontology Class
---

# beneficial ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwnership>

## Definition

situation linking party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner) to the asset that they own

## Relationships

- **Subclass of**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)

## Constraints

- **[hasOwnedAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwnedAsset.md)**: some values from of type [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **[hasOwningParty](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwningParty.md)**: some values from of type [BeneficialOwner](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: some values from value `N6ec9848fcf5a4a45801e2f3248a9aa90`

## Annotations

- **label**: beneficial ownership
- **definition**: situation linking party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner) to the asset that they own
- **explanatoryNote**: Beneficial ownership may be shared among a group of individuals. If a beneficial owner acquires a position of more than 5 percent in the United States, it must file Schedule 13D or 13G under Section 12 of the Securities Exchange Act of 1934.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
