---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: common designation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: frequently used designation for an entity
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#AnnotationProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/commonDesignation
sources:
- id: fibo-source-b35d351e6d
  resource: references/fibo/FND/Utilities/AnnotationVocabulary.rdf
  sha256: b35d351e6d0d981175c56d3b40476b13e64e7b6ed90dd4fd030ececd6f23a2dd
  title: FIBO source FND/Utilities/AnnotationVocabulary.rdf
title: common designation
type: Ontology Property
---

# common designation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/commonDesignation>

## Definition

frequently used designation for an entity

## Relationships

- **Subproperty of**: [synonym](<https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym>)

## Annotations

- **label**: common designation
- **definition**: frequently used designation for an entity
- **adaptedFrom**: https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
