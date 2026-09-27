---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: State Street Corporation US-MA
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: publicly held company and for profit corporation legal entity for State Street Corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: State Street Corporation
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.statestreet.com/home.html
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ForProfitCorporation
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/PubliclyHeldCompany
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfMassachusettsJurisdiction.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfMassachusettsJurisdiction
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/StateStreetCorporationHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/StateStreetCorporationHeadquartersAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/StateStreetCorporationIncorporationDate.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfRegistration
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/StateStreetCorporationIncorporationDate
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany
  - predicate: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/StateStreetCorporation-US-MA
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: State Street Corporation US-MA
type: Ontology Individual
---

# State Street Corporation US-MA

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/StateStreetCorporation-US-MA>

## Definition

publicly held company and for profit corporation legal entity for State Street Corporation

## Relationships

- **Related to**: [StateStreetCorporationIncorporationDate](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/StateStreetCorporationIncorporationDate.md)
- **Related to**: [StateOfMassachusettsJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfMassachusettsJurisdiction.md)
- **Related to**: [StateStreetCorporationHeadquartersAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/StateStreetCorporationHeadquartersAddress.md)
- **Related to**: [CorporationTrustCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)

## Annotations

- **label**: State Street Corporation US-MA
- **definition**: publicly held company and for profit corporation legal entity for State Street Corporation
- **hasLegalName**: State Street Corporation
- **hasWebsite**: http://www.statestreet.com/home.html

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
