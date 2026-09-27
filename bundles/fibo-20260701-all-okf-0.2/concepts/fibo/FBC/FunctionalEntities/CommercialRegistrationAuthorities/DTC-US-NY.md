---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: The Depository Trust Company US-NY
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Depository Trust Company legal entity that is a limited-purpose trust company under New York State banking law
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Depository Trust Company
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCC-US-DE.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasDirectOwningEntity
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCC-US-DE
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCHeadquartersAndLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCHeadquartersAndLegalAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCHeadquartersAndLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCHeadquartersAndLegalAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustAndClearingCorporation.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasDomesticUltimateParent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustAndClearingCorporation
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustCompanyOwnership.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasDirectOwnership
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustCompanyOwnership
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTC-US-NY
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: The Depository Trust Company US-NY
type: Ontology Individual
---

# The Depository Trust Company US-NY

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTC-US-NY>

## Definition

Depository Trust Company legal entity that is a limited-purpose trust company under New York State banking law

## Relationships

- **Defined by**: [CommercialRegistrationAuthorities](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md)
- **Related to**: [DTCHeadquartersAndLegalAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCHeadquartersAndLegalAddress.md)
- **Related to**: [DTCHeadquartersAndLegalAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCHeadquartersAndLegalAddress.md)
- **Related to**: [DepositoryTrustAndClearingCorporation](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustAndClearingCorporation.md)
- **Related to**: [DepositoryTrustCompanyOwnership](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustCompanyOwnership.md)
- **Related to**: [DTCC-US-DE](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCC-US-DE.md)

## Annotations

- **label**: The Depository Trust Company US-NY
- **definition**: Depository Trust Company legal entity that is a limited-purpose trust company under New York State banking law
- **hasLegalName**: Depository Trust Company

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
