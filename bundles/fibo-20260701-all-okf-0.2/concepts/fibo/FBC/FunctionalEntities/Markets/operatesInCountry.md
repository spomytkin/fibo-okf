---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: operates in country
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the ISO 3166-1 country in which an exchange, data reporting services provider, or crypto asset services
      provider operates
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Locations/Country
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Locations/hasCountry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: operates in country
type: Ontology Property
---

# operates in country

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry>

## Definition

indicates the ISO 3166-1 country in which an exchange, data reporting services provider, or crypto asset services provider operates

## Relationships

- **Range**: [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **Subproperty of**: [hasCountry](<https://www.omg.org/spec/Commons/Locations/hasCountry>)

## Annotations

- **label**: operates in country
- **definition**: indicates the ISO 3166-1 country in which an exchange, data reporting services provider, or crypto asset services provider operates
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
