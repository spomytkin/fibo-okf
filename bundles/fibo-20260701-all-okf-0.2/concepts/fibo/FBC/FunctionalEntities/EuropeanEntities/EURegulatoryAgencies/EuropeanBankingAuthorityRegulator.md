---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: European Banking Authority (EBA) Regulator
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: European Banking Authority (EBA) regulator and registration authority
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.eba.europa.eu/about-us/missions-and-tasks
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  - https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/EuropeanUnionJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/EuropeanUnionJurisdiction
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/CreditInstitutionRegister.md
    predicate: https://www.omg.org/spec/Commons/Organizations/manages
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/CreditInstitutionRegister
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanBankingAuthority.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanBankingAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanBankingAuthorityRegulator
sources:
- id: fibo-source-ae4bf1d843
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.rdf
  sha256: ae4bf1d8430cf5c1d1d6e3b5004b20bc4d4e330a4cc094c02e2880e7bd06fd6f
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.rdf
title: European Banking Authority (EBA) Regulator
type: Ontology Individual
---

# European Banking Authority (EBA) Regulator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanBankingAuthorityRegulator>

## Definition

European Banking Authority (EBA) regulator and registration authority

## Relationships

- **Related to**: [CreditInstitutionRegister](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/CreditInstitutionRegister.md)
- **Related to**: [EuropeanUnionJurisdiction](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/EuropeanUnionJurisdiction.md)
- **Related to**: [EuropeanBankingAuthority](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanBankingAuthority.md)

## Annotations

- **label**: European Banking Authority (EBA) Regulator
- **definition**: European Banking Authority (EBA) regulator and registration authority
- **adaptedFrom**: http://www.eba.europa.eu/about-us/missions-and-tasks

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
