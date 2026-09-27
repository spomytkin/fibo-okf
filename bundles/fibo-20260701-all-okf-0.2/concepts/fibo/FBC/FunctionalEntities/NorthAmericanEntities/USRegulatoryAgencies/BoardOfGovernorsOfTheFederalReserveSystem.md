---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Board of Governors of the Federal Reserve System
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: regulatory agency and registration authority for the overall Federal Reserve System
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.federalreserve.gov/faqs/about_12591.htm
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateAuthority
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  - https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveBoard.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveBoard
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
- id: fibo-source-0b5fde6ab3
  resource: references/fibo/IND/InterestRates/MarketDataProviders.rdf
  sha256: 0b5fde6ab3fe477e8381e86968420d93073a53e8b18733937a275f845b4e18c4
  title: FIBO source IND/InterestRates/MarketDataProviders.rdf
title: Board of Governors of the Federal Reserve System
type: Ontology Individual
---

# Board of Governors of the Federal Reserve System

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem>

## Definition

regulatory agency and registration authority for the overall Federal Reserve System

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [FederalReserveRegulatoryAgencyAndCentralBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank.md)
- **Related to**: [FederalReserveBoard](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveBoard.md)

## Annotations

- **label**: Board of Governors of the Federal Reserve System
- **definition**: regulatory agency and registration authority for the overall Federal Reserve System
- **adaptedFrom**: http://www.federalreserve.gov/faqs/about_12591.htm

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
