---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: primary address number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: address component that identifies a location with respect to a given street
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Although traditionally called a 'number', the street number may consist of alphanumeric characters, for example,
      '221B'.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: street number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/AddressComponent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressComponent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PrimaryAddressNumber
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: primary address number
type: Ontology Class
---

# primary address number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PrimaryAddressNumber>

## Definition

address component that identifies a location with respect to a given street

## Relationships

- **Subclass of**: [AddressComponent](/concepts/fibo/FND/Places/Addresses/AddressComponent.md)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: primary address number
- **definition**: address component that identifies a location with respect to a given street
- **explanatoryNote**: Although traditionally called a 'number', the street number may consist of alphanumeric characters, for example, '221B'.
- **synonym**: street number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
