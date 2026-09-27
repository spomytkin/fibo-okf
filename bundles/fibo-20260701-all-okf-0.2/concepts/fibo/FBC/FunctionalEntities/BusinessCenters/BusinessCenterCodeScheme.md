---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business center code set
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: coding scheme used to define a set of codes for municipalities or business centers
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.fpml.org/coding-scheme/business-center
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/BusinessCenterCodeScheme
sources:
- id: fibo-source-9bbbd18083
  resource: references/fibo/FBC/FunctionalEntities/BusinessCenters.rdf
  sha256: 9bbbd18083fbf3183af8c86eb613aa661a0110b3c02acb42c40459b17aaefe20
  title: FIBO source FBC/FunctionalEntities/BusinessCenters.rdf
title: business center code set
type: Ontology Class
---

# business center code set

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/BusinessCenterCodeScheme>

## Definition

coding scheme used to define a set of codes for municipalities or business centers

## Relationships

- **Subclass of**: [CodeSet](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet>)

## Annotations

- **label**: business center code set
- **definition**: coding scheme used to define a set of codes for municipalities or business centers
- **adaptedFrom**: http://www.fpml.org/coding-scheme/business-center

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
