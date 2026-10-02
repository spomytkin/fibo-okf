---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is self-maintained
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the information about the entity is maintained internally or by a third-party
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.swift.com/standards/data-standards/bic?tl=en#BICPolicyandDatarecord
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/isSelfMaintained
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: is self-maintained
type: Ontology Property
---

# is self-maintained

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/isSelfMaintained>

## Definition

indicates whether the information about the entity is maintained internally or by a third-party

## Relationships

- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: is self-maintained
- **definition**: indicates whether the information about the entity is maintained internally or by a third-party
- **adaptedFrom**: https://www.swift.com/standards/data-standards/bic?tl=en#BICPolicyandDatarecord

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
