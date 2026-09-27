---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: International Business Machines Corporation US-NY
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: publicly held company and for profit corporation legal entity for International Business Machines Corporation,
      a New York domestic business corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasPriorLegalName
    value: COMPUTING-TABULATING-RECORDING-CO.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasTradingOrOperationalName
    value: IBM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: International Business Machines Corporation
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.ibm.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ForProfitCorporation
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/PubliclyHeldCompany
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfNewYorkJurisdiction.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfNewYorkJurisdiction
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationIncorporationDate.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfIncorporation
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationIncorporationDate
  - predicate: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporation-US-NY
sources:
- id: fibo-source-c449487789
  resource: references/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
  sha256: c4494877893c93f9a616fa9cf3906eba0fb6c3a876878b1cdb60c40b3044436d
  title: FIBO source EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
title: International Business Machines Corporation US-NY
type: Ontology Individual
---

# International Business Machines Corporation US-NY

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporation-US-NY>

## Definition

publicly held company and for profit corporation legal entity for International Business Machines Corporation, a New York domestic business corporation

## Relationships

- **Related to**: [InternationalBusinessMachinesCorporationIncorporationDate](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationIncorporationDate.md)
- **Related to**: [StateOfNewYorkJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfNewYorkJurisdiction.md)
- **Related to**: [InternationalBusinessMachinesCorporationAddress](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationAddress.md)
- **Related to**: [InternationalBusinessMachinesCorporationAddress](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/InternationalBusinessMachinesCorporationAddress.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)

## Annotations

- **label**: International Business Machines Corporation US-NY
- **definition**: publicly held company and for profit corporation legal entity for International Business Machines Corporation, a New York domestic business corporation
- **hasPriorLegalName**: COMPUTING-TABULATING-RECORDING-CO.
- **hasTradingOrOperationalName**: IBM
- **hasLegalName**: International Business Machines Corporation
- **hasWebsite**: https://www.ibm.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
