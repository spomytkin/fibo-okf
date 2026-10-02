---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market identifier code registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in a market identifier code registry that conforms to ISO 10383
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MIC registry entry
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/10383/iso-10383-market-identifier-codes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationRevisionDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasMarketIdentifierCodeStatus
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistryEntry
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: market identifier code registry entry
type: Ontology Class
---

# market identifier code registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistryEntry>

## Definition

entry in a market identifier code registry that conforms to ISO 10383

## Relationships

- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[hasInitialRegistrationDate](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate.md)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasRegistrationRevisionDate](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationRevisionDate.md)**: max qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasMarketIdentifierCodeStatus](/concepts/fibo/FBC/FunctionalEntities/Markets/hasMarketIdentifierCodeStatus.md)**: exact qualified cardinality 1 of type [MarketIdentifierCodeStatus](/concepts/fibo/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [MarketIdentifier](/concepts/fibo/FBC/FunctionalEntities/Markets/MarketIdentifier.md)
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry`

## Annotations

- **label**: market identifier code registry entry
- **definition**: entry in a market identifier code registry that conforms to ISO 10383
- **abbreviation**: MIC registry entry
- **adaptedFrom**: https://www.iso20022.org/10383/iso-10383-market-identifier-codes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
