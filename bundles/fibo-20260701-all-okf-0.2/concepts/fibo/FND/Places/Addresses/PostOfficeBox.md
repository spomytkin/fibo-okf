---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: post office box
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: post office box associated with an address
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Post office box identifiers are only unique to a given jurisdiction, which may be a post office, town, or other
      region.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostOfficeBoxDesignator
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/SupplementalAddressComponent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressComponent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostOfficeBox
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: post office box
type: Ontology Class
---

# post office box

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostOfficeBox>

## Definition

post office box associated with an address

## Relationships

- **Subclass of**: [SupplementalAddressComponent](/concepts/fibo/FND/Places/Addresses/SupplementalAddressComponent.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [PostOfficeBoxDesignator](/concepts/fibo/FND/Places/Addresses/PostOfficeBoxDesignator.md)

## Annotations

- **label**: post office box
- **definition**: post office box associated with an address
- **explanatoryNote**: Post office box identifiers are only unique to a given jurisdiction, which may be a post office, town, or other region.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
