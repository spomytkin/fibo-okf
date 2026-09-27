---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Ohio Business Filing Portal
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry of business entities for businesses that have registered with the Ohio Secretary of State
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistryName
    value: Ohio Business Filing Portal
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.sos.state.oh.us/businesses/
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfOhioJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfOhioJurisdiction
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/OhioBusinessRegistrar.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/OhioBusinessRegistrar
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/OhioBusinessFilingPortal
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Ohio Business Filing Portal
type: Ontology Individual
---

# Ohio Business Filing Portal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/OhioBusinessFilingPortal>

## Definition

registry of business entities for businesses that have registered with the Ohio Secretary of State

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [OhioBusinessRegistrar](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/OhioBusinessRegistrar.md)
- **Related to**: [StateOfOhioJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfOhioJurisdiction.md)

## Annotations

- **label**: Ohio Business Filing Portal
- **definition**: registry of business entities for businesses that have registered with the Ohio Secretary of State
- **hasRegistryName**: Ohio Business Filing Portal
- **hasWebsite**: https://www.sos.state.oh.us/businesses/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
