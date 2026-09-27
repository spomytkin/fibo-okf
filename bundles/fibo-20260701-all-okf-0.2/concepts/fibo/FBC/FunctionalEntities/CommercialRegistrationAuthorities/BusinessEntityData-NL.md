---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Business Entity Data (BED) B.V. NL
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Business Entity Data (BED) B.V. legal entity that is a privately held company in the Netherlands
  - language: nl
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
    value: Besloten Vennootschap
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Business Entity Data (BED) B.V.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/PrivatelyHeldCompany
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityDataHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityDataHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityDataLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityDataLegalAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustAndClearingCorporation.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasGlobalUltimateParent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustAndClearingCorporation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityData-NL
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: Business Entity Data (BED) B.V. NL
type: Ontology Individual
---

# Business Entity Data (BED) B.V. NL

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityData-NL>

## Definition

Business Entity Data (BED) B.V. legal entity that is a privately held company in the Netherlands

## Relationships

- **Related to**: [BusinessEntityDataHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityDataHeadquartersAddress.md)
- **Related to**: [BusinessEntityDataLegalAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityDataLegalAddress.md)
- **Related to**: [DepositoryTrustAndClearingCorporation](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustAndClearingCorporation.md)

## Annotations

- **label**: Business Entity Data (BED) B.V. NL
- **definition**: Business Entity Data (BED) B.V. legal entity that is a privately held company in the Netherlands
- **hasLegalFormAbbreviation** (nl): Besloten Vennootschap
- **hasLegalName**: Business Entity Data (BED) B.V.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
