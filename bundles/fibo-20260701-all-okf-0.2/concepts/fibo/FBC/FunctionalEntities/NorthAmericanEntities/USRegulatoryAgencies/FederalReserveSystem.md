---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Federal Reserve System
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: central banking system of the U.S., comprised of the Federal Reserve Board, the 12 Federal Reserve Banks, the Federal
      Open Market Committee, and the national and state member banks
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FRS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Federal Reserve, the central bank of the United States, provides the nation with a safe, flexible, and stable
      monetary and financial system.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Fed
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Federal Reserve
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.federalreserve.gov/
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAgency
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalGovernmentEntity
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesGovernment.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesGovernment
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystem
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Federal Reserve System
type: Ontology Individual
---

# Federal Reserve System

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystem>

## Definition

central banking system of the U.S., comprised of the Federal Reserve Board, the 12 Federal Reserve Banks, the Federal Open Market Committee, and the national and state member banks

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [UnitedStatesGovernment](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesGovernment.md)
- **Related to**: [UnitedStatesJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md)

## Annotations

- **label**: Federal Reserve System
- **definition**: central banking system of the U.S., comprised of the Federal Reserve Board, the 12 Federal Reserve Banks, the Federal Open Market Committee, and the national and state member banks
- **abbreviation**: FRS
- **explanatoryNote**: The Federal Reserve, the central bank of the United States, provides the nation with a safe, flexible, and stable monetary and financial system.
- **synonym**: Fed
- **synonym**: Federal Reserve
- **hasWebsite**: https://www.federalreserve.gov/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
