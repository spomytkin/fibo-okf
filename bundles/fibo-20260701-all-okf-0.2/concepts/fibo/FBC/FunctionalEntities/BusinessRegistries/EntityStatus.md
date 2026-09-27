---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entity status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: lifecycle stage indicating the operational and/or legal status of an entity
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In some jurisdictions, there may be other possible values for entity status, such as suspended in the State of
      California, thus the individuals provided herein are not intended to be exhaustive.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityStatus
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: entity status
type: Ontology Class
---

# entity status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityStatus>

## Definition

lifecycle stage indicating the operational and/or legal status of an entity

## Relationships

- **Subclass of**: [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)

## Annotations

- **label**: entity status
- **definition**: lifecycle stage indicating the operational and/or legal status of an entity
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
- **explanatoryNote**: In some jurisdictions, there may be other possible values for entity status, such as suspended in the State of California, thus the individuals provided herein are not intended to be exhaustive.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
