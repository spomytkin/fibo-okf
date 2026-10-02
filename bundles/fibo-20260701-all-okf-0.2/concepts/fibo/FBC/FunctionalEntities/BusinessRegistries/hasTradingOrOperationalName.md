---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has trading or operational name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: denotes a 'trading as', 'brand name', 'doing business as', or 'operating under' name currently used by the entity
      in addition to, but not replacing, the (primary) legal, official registered name
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Designators/hasTextualName
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasTradingOrOperationalName
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: has trading or operational name
type: Ontology Property
---

# has trading or operational name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasTradingOrOperationalName>

## Definition

denotes a 'trading as', 'brand name', 'doing business as', or 'operating under' name currently used by the entity in addition to, but not replacing, the (primary) legal, official registered name

## Relationships

- **Subproperty of**: [hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)

## Annotations

- **label**: has trading or operational name
- **definition**: denotes a 'trading as', 'brand name', 'doing business as', or 'operating under' name currently used by the entity in addition to, but not replacing, the (primary) legal, official registered name
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
