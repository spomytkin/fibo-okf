---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: JPMorgan Chase & Co. US-DE
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: publicly held company and for profit corporation legal entity for the JPMorgan Chase & Co., a Delaware Corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: JPMorgan Chase & Co.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.jpmorganchase.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ForProfitCorporation
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/PubliclyHeldCompany
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoHeadquartersAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoIncorporationDate.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfRegistration
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoIncorporationDate
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany
  - predicate: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCo-US-DE
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: JPMorgan Chase & Co. US-DE
type: Ontology Individual
---

# JPMorgan Chase & Co. US-DE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCo-US-DE>

## Definition

publicly held company and for profit corporation legal entity for the JPMorgan Chase & Co., a Delaware Corporation

## Relationships

- **Related to**: [JPMorganChaseAndCoIncorporationDate](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoIncorporationDate.md)
- **Related to**: [StateOfDelawareJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md)
- **Related to**: [JPMorganChaseAndCoHeadquartersAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoHeadquartersAddress.md)
- **Related to**: [CorporationTrustCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)

## Annotations

- **label**: JPMorgan Chase & Co. US-DE
- **definition**: publicly held company and for profit corporation legal entity for the JPMorgan Chase & Co., a Delaware Corporation
- **hasLegalName**: JPMorgan Chase & Co.
- **hasWebsite**: https://www.jpmorganchase.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
