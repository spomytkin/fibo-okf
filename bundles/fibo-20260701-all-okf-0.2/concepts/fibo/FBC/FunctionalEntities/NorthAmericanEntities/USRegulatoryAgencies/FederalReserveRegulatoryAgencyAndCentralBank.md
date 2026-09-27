---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Federal Reserve regulatory agency and central bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: regulatory agency and registration authority role of the Federal Reserve System
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/PrimaryFederalRegulator
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystem.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystem
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository.md
    predicate: https://www.omg.org/spec/Commons/Organizations/manages
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.federalreserve.gov/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Federal Reserve regulatory agency and central bank
type: Ontology Individual
---

# Federal Reserve regulatory agency and central bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank>

## Definition

regulatory agency and registration authority role of the Federal Reserve System

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [NationalInformationCenterRepository](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository.md)
- **Related to**: [FederalReserveSystem](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystem.md)
- **See also**: [http://www.federalreserve.gov/](<http://www.federalreserve.gov/>)

## Annotations

- **label**: Federal Reserve regulatory agency and central bank
- **definition**: regulatory agency and registration authority role of the Federal Reserve System

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
