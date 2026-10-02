---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: WFC Holdings, LLC US-DE
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: private company with limited liability legal entity for WFC Holdings, LLC legal entity, a Delaware Limited Liability
      Corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasPriorLegalName
    value: WFC Holdings Corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: WFC Holdings, LLC
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/isOrganizedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLCHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLCHeadquartersAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLCIncorporationDate.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfIncorporation
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLCIncorporationDate
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoAndCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasDomesticUltimateParent
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoAndCompany
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoBankNationalAssociation.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasSubsidiary
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoBankNationalAssociation
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany
  - predicate: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLC-US-DE
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: WFC Holdings, LLC US-DE
type: Ontology Individual
---

# WFC Holdings, LLC US-DE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLC-US-DE>

## Definition

private company with limited liability legal entity for WFC Holdings, LLC legal entity, a Delaware Limited Liability Corporation

## Relationships

- **Related to**: [WFCHoldingsLLCIncorporationDate](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLCIncorporationDate.md)
- **Related to**: [WFCHoldingsLLCHeadquartersAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLCHeadquartersAddress.md)
- **Related to**: [WellsFargoAndCompany](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoAndCompany.md)
- **Related to**: [WellsFargoBankNationalAssociation](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoBankNationalAssociation.md)
- **Related to**: [CorporationServiceCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [StateOfDelawareJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md)

## Annotations

- **label**: WFC Holdings, LLC US-DE
- **definition**: private company with limited liability legal entity for WFC Holdings, LLC legal entity, a Delaware Limited Liability Corporation
- **hasPriorLegalName**: WFC Holdings Corporation
- **hasLegalName**: WFC Holdings, LLC

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
