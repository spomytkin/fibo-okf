---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ABA RTN registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an entry in the ABA RTN registry, a repository of financial institution characteristics collected by the ABA Registrar
      on behalf of the ABA
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/RoutingTransitNumber
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistry
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistryEntry
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: ABA RTN registry entry
type: Ontology Class
---

# ABA RTN registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistryEntry>

## Definition

an entry in the ABA RTN registry, a repository of financial institution characteristics collected by the ABA Registrar on behalf of the ABA

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [RoutingTransitNumber](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/RoutingTransitNumber.md)
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistry`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: all values from of type [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label**: ABA RTN registry entry
- **definition**: an entry in the ABA RTN registry, a repository of financial institution characteristics collected by the ABA Registrar on behalf of the ABA

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
