---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business center code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: code used to denote a metropolitan area where business is conducted
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.fpml.org/coding-scheme/business-center
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The codes for business centers and municipalities defined herein are largely those identified either as FpML business
      centers or are locations where there is an exchange, as noted in the ISO 10962 MIC code standard.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/BusinessCenter
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/BusinessCenterCode
sources:
- id: fibo-source-9bbbd18083
  resource: references/fibo/FBC/FunctionalEntities/BusinessCenters.rdf
  sha256: 9bbbd18083fbf3183af8c86eb613aa661a0110b3c02acb42c40459b17aaefe20
  title: FIBO source FBC/FunctionalEntities/BusinessCenters.rdf
title: business center code
type: Ontology Class
---

# business center code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/BusinessCenterCode>

## Definition

code used to denote a metropolitan area where business is conducted

## Relationships

- **Subclass of**: [GeographicRegionIdentifier](<https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [BusinessCenter](<https://www.omg.org/spec/Commons/Locations/BusinessCenter>)

## Annotations

- **label**: business center code
- **definition**: code used to denote a metropolitan area where business is conducted
- **adaptedFrom**: http://www.fpml.org/coding-scheme/business-center
- **explanatoryNote**: The codes for business centers and municipalities defined herein are largely those identified either as FpML business centers or are locations where there is an exchange, as noted in the ISO 10962 MIC code standard.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
