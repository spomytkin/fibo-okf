---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Consumer Financial Protection Bureau
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Consumer Financial Protection Bureau (CFPB), an independent Federal agency that helps consumer finance markets
      work by making rules more effective, by consistently and fairly enforcing those rules, and by empowering consumers to
      take more control over their economic lives
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CFPB
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.consumerfinance.gov/
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentDepartment
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalGovernmentEntity
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/USDepartmentOfTheTreasury.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/USDepartmentOfTheTreasury
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ConsumerFinancialProtectionBureau
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Consumer Financial Protection Bureau
type: Ontology Individual
---

# Consumer Financial Protection Bureau

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ConsumerFinancialProtectionBureau>

## Definition

Consumer Financial Protection Bureau (CFPB), an independent Federal agency that helps consumer finance markets work by making rules more effective, by consistently and fairly enforcing those rules, and by empowering consumers to take more control over their economic lives

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [USDepartmentOfTheTreasury](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/USDepartmentOfTheTreasury.md)
- **Related to**: [UnitedStatesJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md)

## Annotations

- **label**: Consumer Financial Protection Bureau
- **definition**: Consumer Financial Protection Bureau (CFPB), an independent Federal agency that helps consumer finance markets work by making rules more effective, by consistently and fairly enforcing those rules, and by empowering consumers to take more control over their economic lives
- **abbreviation**: CFPB
- **hasWebsite**: https://www.consumerfinance.gov/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
