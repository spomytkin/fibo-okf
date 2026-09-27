---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: JPMorgan Chase Bank, National Association US
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: business entity for JPMorgan Chase Bank, National Association, a national banking entity established under the
      National Banking Act of 1864
  - predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
    value: National Bank (en), 62VJ
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasTradingOrOperationalName
    value: JPMorgan Chase Bank, N.A.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: JPMorgan Chase Bank, National Association
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.chase.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasDomesticUltimateParent
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCo
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoHeadquartersAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseBankNationalAssociationAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseBankNationalAssociationAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseBankNationalAssociationRegistrationDate.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfRegistration
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseBankNationalAssociationRegistrationDate
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany
  - predicate: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseBankNationalAssociation-US
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: JPMorgan Chase Bank, National Association US
type: Ontology Individual
---

# JPMorgan Chase Bank, National Association US

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseBankNationalAssociation-US>

## Definition

business entity for JPMorgan Chase Bank, National Association, a national banking entity established under the National Banking Act of 1864

## Relationships

- **Related to**: [JPMorganChaseBankNationalAssociationRegistrationDate](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseBankNationalAssociationRegistrationDate.md)
- **Related to**: [JPMorganChaseBankNationalAssociationAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseBankNationalAssociationAddress.md)
- **Related to**: [JPMorganChaseAndCoHeadquartersAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCoHeadquartersAddress.md)
- **Related to**: [JPMorganChaseAndCo](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganChaseAndCo.md)
- **Related to**: [CorporationTrustCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)

## Annotations

- **label**: JPMorgan Chase Bank, National Association US
- **definition**: business entity for JPMorgan Chase Bank, National Association, a national banking entity established under the National Banking Act of 1864
- **hasLegalFormAbbreviation**: National Bank (en), 62VJ
- **hasTradingOrOperationalName**: JPMorgan Chase Bank, N.A.
- **hasLegalName**: JPMorgan Chase Bank, National Association
- **hasWebsite**: https://www.chase.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
