---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ABA RTN Registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: American Bankers Association (ABA) Routing Transit Number (RTN) registry, a repository of institution characteristics
      for those that have assigned RTNs, managed by the ABA's designated registration authority (RA)
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRTNRegistrar.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRTNRegistrar
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistry
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: ABA RTN Registry
type: Ontology Individual
---

# ABA RTN Registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistry>

## Definition

American Bankers Association (ABA) Routing Transit Number (RTN) registry, a repository of institution characteristics for those that have assigned RTNs, managed by the ABA's designated registration authority (RA)

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [AmericanBankersAssociationRTNRegistrar](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRTNRegistrar.md)

## Annotations

- **label**: ABA RTN Registry
- **definition**: American Bankers Association (ABA) Routing Transit Number (RTN) registry, a repository of institution characteristics for those that have assigned RTNs, managed by the ABA's designated registration authority (RA)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
