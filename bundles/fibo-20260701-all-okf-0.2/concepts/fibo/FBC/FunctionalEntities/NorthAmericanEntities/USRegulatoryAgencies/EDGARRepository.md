---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: EDGAR Repository
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: EDGAR repository, a repository of financial information about securities and their issuers, including but not limited
      to corporate quarterly and annual filings, collected by the SEC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.sec.gov/edgar/aboutedgar.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: EDGAR, the Electronic Data Gathering, Analysis, and Retrieval system, performs automated collection, validation,
      indexing, acceptance, and forwarding of submissions by companies and others who are required by law to file forms with
      the U.S. Securities and Exchange Commission (SEC). Its primary purpose is to increase the efficiency and fairness of
      the securities market for the benefit of investors, corporations, and the economy by accelerating the receipt, acceptance,
      dissemination, and analysis of time-sensitive corporate information filed with the agency.
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/EDGARRepository
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: EDGAR Repository
type: Ontology Individual
---

# EDGAR Repository

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/EDGARRepository>

## Definition

EDGAR repository, a repository of financial information about securities and their issuers, including but not limited to corporate quarterly and annual filings, collected by the SEC

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [SecuritiesAndExchangeRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator.md)

## Annotations

- **label**: EDGAR Repository
- **definition**: EDGAR repository, a repository of financial information about securities and their issuers, including but not limited to corporate quarterly and annual filings, collected by the SEC
- **adaptedFrom**: http://www.sec.gov/edgar/aboutedgar.htm
- **explanatoryNote**: EDGAR, the Electronic Data Gathering, Analysis, and Retrieval system, performs automated collection, validation, indexing, acceptance, and forwarding of submissions by companies and others who are required by law to file forms with the U.S. Securities and Exchange Commission (SEC). Its primary purpose is to increase the efficiency and fairness of the securities market for the benefit of investors, corporations, and the economy by accelerating the receipt, acceptance, dissemination, and analysis of time-sensitive corporate information filed with the agency.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
