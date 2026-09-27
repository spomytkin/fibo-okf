---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business identifier code data record
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in a registry that conforms to ISO 9362 for the management of BIC codes and related registration information
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BIC data record
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.swift.com/standards/data-standards/bic
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/isSelfMaintained
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeDataRecord
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: business identifier code data record
type: Ontology Class
---

# business identifier code data record

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeDataRecord>

## Definition

entry in a registry that conforms to ISO 9362 for the management of BIC codes and related registration information

## Relationships

- **Subclass of**: [BusinessRegistryEntry](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md)

## Constraints

- **[isSelfMaintained](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/isSelfMaintained.md)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [BusinessIdentifierCode](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode.md)
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry`

## Annotations

- **label**: business identifier code data record
- **definition**: entry in a registry that conforms to ISO 9362 for the management of BIC codes and related registration information
- **abbreviation**: BIC data record
- **adaptedFrom**: https://www.swift.com/standards/data-standards/bic

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
