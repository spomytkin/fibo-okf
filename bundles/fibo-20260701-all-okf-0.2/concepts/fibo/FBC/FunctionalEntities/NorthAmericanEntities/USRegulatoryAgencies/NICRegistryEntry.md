---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: National Information Center (NIC) registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an entry in the the National Information Center (NIC) repository, a repository of financial data and institution
      characteristics collected by the Federal Reserve System
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.ffiec.gov/nicpubweb/nicweb/NicHome.aspx
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ResearchStatisticsSupervisionDiscountIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NICRegistryEntry
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: National Information Center (NIC) registry entry
type: Ontology Class
---

# National Information Center (NIC) registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NICRegistryEntry>

## Definition

an entry in the the National Information Center (NIC) repository, a repository of financial data and institution characteristics collected by the Federal Reserve System

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [ResearchStatisticsSupervisionDiscountIdentifier](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ResearchStatisticsSupervisionDiscountIdentifier.md)
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: all values from of type [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Annotations

- **label**: National Information Center (NIC) registry entry
- **definition**: an entry in the the National Information Center (NIC) repository, a repository of financial data and institution characteristics collected by the Federal Reserve System
- **adaptedFrom**: http://www.ffiec.gov/nicpubweb/nicweb/NicHome.aspx

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
