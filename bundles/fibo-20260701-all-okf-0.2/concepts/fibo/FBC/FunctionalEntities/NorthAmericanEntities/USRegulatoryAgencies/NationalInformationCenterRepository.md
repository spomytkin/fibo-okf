---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: National Information Center (NIC) Repository
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: National Information Center (NIC) repository, a repository of financial data and institution characteristics collected
      by the Federal Reserve System
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The National Information Center (NIC)repository provides comprehensive information on banks and other institutions
      for which the Federal Reserve has a supervisory, regulatory, or research interest including both domestic and foreign
      banking organizations operating in the U.S.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.ffiec.gov/nicpubweb/nicweb/NicHome.aspx
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.ffiec.gov/nicpubweb/content/DataDownload/NPW%20Data%20Dictionary.pdf/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: National Information Center (NIC) Repository
type: Ontology Individual
---

# National Information Center (NIC) Repository

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository>

## Definition

National Information Center (NIC) repository, a repository of financial data and institution characteristics collected by the Federal Reserve System

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [FederalReserveRegulatoryAgencyAndCentralBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank.md)
- **See also**: [NPW%20Data%20Dictionary.pdf](<https://www.ffiec.gov/nicpubweb/content/DataDownload/NPW%20Data%20Dictionary.pdf/>)

## Annotations

- **label**: National Information Center (NIC) Repository
- **definition**: National Information Center (NIC) repository, a repository of financial data and institution characteristics collected by the Federal Reserve System
- **explanatoryNote**: The National Information Center (NIC)repository provides comprehensive information on banks and other institutions for which the Federal Reserve has a supervisory, regulatory, or research interest including both domestic and foreign banking organizations operating in the U.S.
- **hasWebsite**: http://www.ffiec.gov/nicpubweb/nicweb/NicHome.aspx

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
