---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Apple Inc. business entity identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registration identifier assigned by the California Department of Corporations for Apple Inc.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate
    value: '1977-01-03'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: '806592'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifier
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfCaliforniaJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfCaliforniaJurisdiction
  - concept: /concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AppleInc-US-CA.md
    predicate: https://www.omg.org/spec/Commons/Identifiers/identifies
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AppleInc-US-CA
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/ActiveStatus.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasEntityStatus
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/ActiveStatus
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CaliforniaBusinessEntitiesRegistry.md
    predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CaliforniaBusinessEntitiesRegistry
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CaliforniaBusinessRegistrationIdentifierScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CaliforniaBusinessRegistrationIdentifierScheme
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://bizfileonline.sos.ca.gov/search/business
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AppleIncBusinessEntityIdentifier
sources:
- id: fibo-source-c449487789
  resource: references/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
  sha256: c4494877893c93f9a616fa9cf3906eba0fb6c3a876878b1cdb60c40b3044436d
  title: FIBO source EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
title: Apple Inc. business entity identifier
type: Ontology Individual
---

# Apple Inc. business entity identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AppleIncBusinessEntityIdentifier>

## Definition

registration identifier assigned by the California Department of Corporations for Apple Inc.

## Relationships

- **Related to**: [ActiveStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/ActiveStatus.md)
- **Related to**: [CaliforniaBusinessRegistrationIdentifierScheme](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CaliforniaBusinessRegistrationIdentifierScheme.md)
- **Related to**: [AppleInc-US-CA](/concepts/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/AppleInc-US-CA.md)
- **Related to**: [CaliforniaBusinessEntitiesRegistry](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CaliforniaBusinessEntitiesRegistry.md)
- **Related to**: [StateOfCaliforniaJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfCaliforniaJurisdiction.md)
- **See also**: [business](<https://bizfileonline.sos.ca.gov/search/business>)

## Annotations

- **label**: Apple Inc. business entity identifier
- **definition**: registration identifier assigned by the California Department of Corporations for Apple Inc.
- **hasInitialRegistrationDate**: 1977-01-03
- **hasTag**: 806592

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
