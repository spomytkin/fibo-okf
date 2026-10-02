---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statistical area identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier for a physical location that is defined per a nationally consistent program for designating geographic
      regions for the purposes of tabulating and presenting statistical data
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/display/IND/Statistics+Canada+Census+Information
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalArea
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalAreaIdentifier
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: statistical area identifier
type: Ontology Class
---

# statistical area identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalAreaIdentifier>

## Definition

identifier for a physical location that is defined per a nationally consistent program for designating geographic regions for the purposes of tabulating and presenting statistical data

## Relationships

- **Subclass of**: [GeographicRegionIdentifier](<https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [StatisticalArea](/concepts/fibo/FND/Utilities/Analytics/StatisticalArea.md)

## Annotations

- **label**: statistical area identifier
- **definition**: identifier for a physical location that is defined per a nationally consistent program for designating geographic regions for the purposes of tabulating and presenting statistical data
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/display/IND/Statistics+Canada+Census+Information
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
