---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Alphabet Inc. US-CA
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: publicly held company and for profit corporation legal entity for Alphabet Inc., a Delaware stock corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasTradingOrOperationalName
    value: Alphabet
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Alphabet Inc.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://abc.xyz/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ForProfitCorporation
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/PubliclyHeldCompany
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AlphabetIncCorporateAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AlphabetIncCorporateAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AlphabetIncIncorporationDate.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfIncorporation
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AlphabetIncIncorporationDate
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany
  - predicate: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AlphabetInc-US-CA
sources:
- id: fibo-source-c449487789
  resource: references/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
  sha256: c4494877893c93f9a616fa9cf3906eba0fb6c3a876878b1cdb60c40b3044436d
  title: FIBO source EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
title: Alphabet Inc. US-CA
type: Ontology Individual
---

# Alphabet Inc. US-CA

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AlphabetInc-US-CA>

## Definition

publicly held company and for profit corporation legal entity for Alphabet Inc., a Delaware stock corporation

## Relationships

- **Related to**: [AlphabetIncIncorporationDate](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AlphabetIncIncorporationDate.md)
- **Related to**: [StateOfDelawareJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md)
- **Related to**: [AlphabetIncCorporateAddress](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AlphabetIncCorporateAddress.md)
- **Related to**: [CorporationServiceCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)

## Annotations

- **label**: Alphabet Inc. US-CA
- **definition**: publicly held company and for profit corporation legal entity for Alphabet Inc., a Delaware stock corporation
- **hasTradingOrOperationalName**: Alphabet
- **hasLegalName**: Alphabet Inc.
- **hasWebsite**: https://abc.xyz/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
