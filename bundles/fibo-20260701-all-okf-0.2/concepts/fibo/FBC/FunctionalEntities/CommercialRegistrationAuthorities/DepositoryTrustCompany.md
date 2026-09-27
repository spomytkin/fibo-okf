---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Depository Trust Company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: central counterparty clearing house (CCP), securities depository, and registration authority (RA) functional entity
      for The Depository Trust Company
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: DTC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'DTCC''s subsidiary, The Depository Trust Company (DTC), established in 1973, was created to reduce costs and provide
      clearing and settlement efficiencies by immobilizing securities and making ''book-entry'' changes to ownership of the
      securities.


      DTC brings efficiency to the securities industry by retaining custody of more than 3.5 million securities issues valued
      at US$37.2 trillion, including securities issued in the US and more than 131 countries and territories.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralCounterpartyClearingHouse
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralSecuritiesDepository
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTC-US-NY.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTC-US-NY
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/hasPrimaryFederalRegulator
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator.md
    predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.dtcc.com/about/businesses-and-subsidiaries/dtc.aspx
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustCompany
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Depository Trust Company
type: Ontology Individual
---

# Depository Trust Company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DepositoryTrustCompany>

## Definition

central counterparty clearing house (CCP), securities depository, and registration authority (RA) functional entity for The Depository Trust Company

## Relationships

- **Related to**: [FederalReserveRegulatoryAgencyAndCentralBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank.md)
- **Related to**: [SecuritiesAndExchangeRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator.md)
- **Related to**: [DTC-US-NY](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTC-US-NY.md)
- **See also**: [dtc.aspx](<http://www.dtcc.com/about/businesses-and-subsidiaries/dtc.aspx>)

## Annotations

- **label**: Depository Trust Company
- **definition**: central counterparty clearing house (CCP), securities depository, and registration authority (RA) functional entity for The Depository Trust Company
- **abbreviation**: DTC
- **explanatoryNote**: DTCC's subsidiary, The Depository Trust Company (DTC), established in 1973, was created to reduce costs and provide clearing and settlement efficiencies by immobilizing securities and making 'book-entry' changes to ownership of the securities.  DTC brings efficiency to the securities industry by retaining custody of more than 3.5 million securities issues valued at US$37.2 trillion, including securities issued in the US and more than 131 countries and territories.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
