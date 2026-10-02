---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: European banking regulatory agency and central bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: regulatory agency, registration authority and central banking role of the European Central Bank
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ecb.europa.eu/home/html/index.en.html
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateAuthority
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  - https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/EuropeanUnionJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/EuropeanUnionJurisdiction
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanCentralBank.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanCentralBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanBankingRegulatoryAgencyAndCentralBank
sources:
- id: fibo-source-ae4bf1d843
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.rdf
  sha256: ae4bf1d8430cf5c1d1d6e3b5004b20bc4d4e330a4cc094c02e2880e7bd06fd6f
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.rdf
- id: fibo-source-0b5fde6ab3
  resource: references/fibo/IND/InterestRates/MarketDataProviders.rdf
  sha256: 0b5fde6ab3fe477e8381e86968420d93073a53e8b18733937a275f845b4e18c4
  title: FIBO source IND/InterestRates/MarketDataProviders.rdf
title: European banking regulatory agency and central bank
type: Ontology Individual
---

# European banking regulatory agency and central bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanBankingRegulatoryAgencyAndCentralBank>

## Definition

regulatory agency, registration authority and central banking role of the European Central Bank

## Relationships

- **Related to**: [EuropeanUnionJurisdiction](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/EuropeanUnionJurisdiction.md)
- **Related to**: [EuropeanCentralBank](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanCentralBank.md)

## Annotations

- **label**: European banking regulatory agency and central bank
- **definition**: regulatory agency, registration authority and central banking role of the European Central Bank
- **adaptedFrom**: https://www.ecb.europa.eu/home/html/index.en.html

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
