---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: DTCC US-DE
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The Depository Trust & Clearing Corporation (DTCC) legal entity that is a Delaware corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: DTCC INC.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/StockCorporation
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityData.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasSubsidiary
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityData
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCLegalAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasSubsidiary
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCC-US-DE
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: DTCC US-DE
type: Ontology Individual
---

# DTCC US-DE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCC-US-DE>

## Definition

The Depository Trust & Clearing Corporation (DTCC) legal entity that is a Delaware corporation

## Relationships

- **Related to**: [DTCCHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCHeadquartersAddress.md)
- **Related to**: [DTCCLegalAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCLegalAddress.md)
- **Related to**: [BusinessEntityData](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BusinessEntityData.md)
- **Related to**: [DepositoryTrustCompany](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustCompany.md)

## Annotations

- **label**: DTCC US-DE
- **definition**: The Depository Trust & Clearing Corporation (DTCC) legal entity that is a Delaware corporation
- **hasLegalName**: DTCC INC.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
