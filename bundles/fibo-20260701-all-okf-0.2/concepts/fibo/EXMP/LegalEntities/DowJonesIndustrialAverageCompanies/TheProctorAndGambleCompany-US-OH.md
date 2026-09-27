---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: The Proctor & Gamble Company US-OH
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: publicly held company and for profit corporation legal entity for The Proctor & Gamble Company, an Ohio corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: The Proctor & Gamble Company
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://us.pg.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ForProfitCorporation
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/PubliclyHeldCompany
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfOhioJurisdiction.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfOhioJurisdiction
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheProctorAndGambleCompanyCorporateAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheProctorAndGambleCompanyCorporateAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheProctorAndGambleCompanyIncorporationDate.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfIncorporation
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheProctorAndGambleCompanyIncorporationDate
  - predicate: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheProctorAndGambleCompany-US-OH
sources:
- id: fibo-source-c449487789
  resource: references/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
  sha256: c4494877893c93f9a616fa9cf3906eba0fb6c3a876878b1cdb60c40b3044436d
  title: FIBO source EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
title: The Proctor & Gamble Company US-OH
type: Ontology Individual
---

# The Proctor & Gamble Company US-OH

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheProctorAndGambleCompany-US-OH>

## Definition

publicly held company and for profit corporation legal entity for The Proctor & Gamble Company, an Ohio corporation

## Relationships

- **Related to**: [TheProctorAndGambleCompanyIncorporationDate](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheProctorAndGambleCompanyIncorporationDate.md)
- **Related to**: [StateOfOhioJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfOhioJurisdiction.md)
- **Related to**: [TheProctorAndGambleCompanyCorporateAddress](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheProctorAndGambleCompanyCorporateAddress.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)

## Annotations

- **label**: The Proctor & Gamble Company US-OH
- **definition**: publicly held company and for profit corporation legal entity for The Proctor & Gamble Company, an Ohio corporation
- **hasLegalName**: The Proctor & Gamble Company
- **hasWebsite**: https://us.pg.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
