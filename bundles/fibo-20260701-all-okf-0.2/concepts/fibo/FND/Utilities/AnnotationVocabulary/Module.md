---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: module
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier used to indicate a category used to modularize something based on principles of the model driven architecture
      methodology (MDA), including but not limited to separation of concerns, coherence, and establishing clear logical boundaries
      in order to increase reusability and maintainability
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A module should be designed to reflect these principles, including a small number of models that have well-defined
      relationships with one another, that form a coherent and cohesive whole for some purpose, and that have clear boundaries
      or interfaces to other modules.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Module
sources:
- id: fibo-source-b35d351e6d
  resource: references/fibo/FND/Utilities/AnnotationVocabulary.rdf
  sha256: b35d351e6d0d981175c56d3b40476b13e64e7b6ed90dd4fd030ececd6f23a2dd
  title: FIBO source FND/Utilities/AnnotationVocabulary.rdf
title: module
type: Ontology Class
---

# module

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Module>

## Definition

classifier used to indicate a category used to modularize something based on principles of the model driven architecture methodology (MDA), including but not limited to separation of concerns, coherence, and establishing clear logical boundaries in order to increase reusability and maintainability

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Annotations

- **label**: module
- **definition**: classifier used to indicate a category used to modularize something based on principles of the model driven architecture methodology (MDA), including but not limited to separation of concerns, coherence, and establishing clear logical boundaries in order to increase reusability and maintainability
- **explanatoryNote**: A module should be designed to reflect these principles, including a small number of models that have well-defined relationships with one another, that form a coherent and cohesive whole for some purpose, and that have clear boundaries or interfaces to other modules.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
