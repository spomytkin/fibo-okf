---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: term origin
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: document or other source from which a given term was taken directly; the range for this annotation can be a string,
      URI, or BibliographicCitation
  rdf_types:
  - http://www.w3.org/2002/07/owl#AnnotationProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/directSource
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/termOrigin
sources:
- id: fibo-source-b35d351e6d
  resource: references/fibo/FND/Utilities/AnnotationVocabulary.rdf
  sha256: b35d351e6d0d981175c56d3b40476b13e64e7b6ed90dd4fd030ececd6f23a2dd
  title: FIBO source FND/Utilities/AnnotationVocabulary.rdf
title: term origin
type: Ontology Property
---

# term origin

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/termOrigin>

## Definition

document or other source from which a given term was taken directly; the range for this annotation can be a string, URI, or BibliographicCitation

## Relationships

- **Subproperty of**: [directSource](<https://www.omg.org/spec/Commons/AnnotationVocabulary/directSource>)

## Annotations

- **label**: term origin
- **definition**: document or other source from which a given term was taken directly; the range for this annotation can be a string, URI, or BibliographicCitation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
