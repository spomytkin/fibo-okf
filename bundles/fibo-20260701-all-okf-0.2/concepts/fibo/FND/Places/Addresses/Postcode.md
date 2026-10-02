---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: postcode
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters used to assist in the sorting of mail
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: postal code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostCodeArea
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Postcode
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: postcode
type: Ontology Class
---

# postcode

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Postcode>

## Definition

sequence of characters used to assist in the sorting of mail

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)
- **Subclass of**: [GeographicRegionIdentifier](<https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [PostCodeArea](/concepts/fibo/FND/Places/Addresses/PostCodeArea.md)

## Annotations

- **label** (en): postcode
- **definition**: sequence of characters used to assist in the sorting of mail
- **synonym**: postal code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
