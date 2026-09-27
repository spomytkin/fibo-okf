---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statistical area
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical location that is defined per some program for designating geographic regions for the purposes of tabulating
      and presenting statistical data
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/display/IND/Statistics+Canada+Census+Information
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalAreaIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/GeographicRegion
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalArea
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: statistical area
type: Ontology Class
---

# statistical area

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalArea>

## Definition

physical location that is defined per some program for designating geographic regions for the purposes of tabulating and presenting statistical data

## Relationships

- **Subclass of**: [GeographicRegion](<https://www.omg.org/spec/Commons/Locations/GeographicRegion>)

## Constraints

- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: some values from of type [StatisticalAreaIdentifier](/concepts/fibo/FND/Utilities/Analytics/StatisticalAreaIdentifier.md)

## Annotations

- **label**: statistical area
- **definition**: physical location that is defined per some program for designating geographic regions for the purposes of tabulating and presenting statistical data
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/display/IND/Statistics+Canada+Census+Information
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
