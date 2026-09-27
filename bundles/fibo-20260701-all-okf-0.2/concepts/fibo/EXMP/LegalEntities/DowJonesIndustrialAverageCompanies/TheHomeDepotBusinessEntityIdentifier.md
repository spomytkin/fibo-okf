---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: The Home Depot, Inc. business entity identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registration identifier assigned by the Delaware Division of Corporations for The Home Depot, Inc.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate
    value: '1978-06-29'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: '856429'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifier
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheHomeDepotInc-US-DE.md
    predicate: https://www.omg.org/spec/Commons/Identifiers/identifies
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheHomeDepotInc-US-DE
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/ActiveStatus.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasEntityStatus
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/ActiveStatus
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/DelawareBusinessEntitiesRegistry.md
    predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/DelawareBusinessEntitiesRegistry
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/DelawareBusinessRegistrationIdentifierScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/DelawareBusinessRegistrationIdentifierScheme
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheHomeDepotBusinessEntityIdentifier
sources:
- id: fibo-source-c449487789
  resource: references/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
  sha256: c4494877893c93f9a616fa9cf3906eba0fb6c3a876878b1cdb60c40b3044436d
  title: FIBO source EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
title: The Home Depot, Inc. business entity identifier
type: Ontology Individual
---

# The Home Depot, Inc. business entity identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheHomeDepotBusinessEntityIdentifier>

## Definition

registration identifier assigned by the Delaware Division of Corporations for The Home Depot, Inc.

## Relationships

- **Related to**: [ActiveStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/ActiveStatus.md)
- **Related to**: [DelawareBusinessRegistrationIdentifierScheme](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/DelawareBusinessRegistrationIdentifierScheme.md)
- **Related to**: [TheHomeDepotInc-US-DE](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheHomeDepotInc-US-DE.md)
- **Related to**: [DelawareBusinessEntitiesRegistry](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/DelawareBusinessEntitiesRegistry.md)
- **Related to**: [StateOfDelawareJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md)

## Annotations

- **label**: The Home Depot, Inc. business entity identifier
- **definition**: registration identifier assigned by the Delaware Division of Corporations for The Home Depot, Inc.
- **hasInitialRegistrationDate**: 1978-06-29
- **hasTag**: 856429

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
