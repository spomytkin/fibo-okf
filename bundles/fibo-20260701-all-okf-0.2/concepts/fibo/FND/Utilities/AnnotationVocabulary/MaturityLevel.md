---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: maturity level
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier used to indicate the state of an artifact with respect to its development lifecycle
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'FIBO currently has three maturity levels: Informative, Provisional, and Release.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/MaturityLevel
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
- id: fibo-source-b35d351e6d
  resource: references/fibo/FND/Utilities/AnnotationVocabulary.rdf
  sha256: b35d351e6d0d981175c56d3b40476b13e64e7b6ed90dd4fd030ececd6f23a2dd
  title: FIBO source FND/Utilities/AnnotationVocabulary.rdf
title: maturity level
type: Ontology Class
---

# maturity level

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/MaturityLevel>

## Definition

classifier used to indicate the state of an artifact with respect to its development lifecycle

## Relationships

- **Subclass of**: [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)
- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Annotations

- **label**: maturity level
- **definition**: classifier used to indicate the state of an artifact with respect to its development lifecycle
- **explanatoryNote** (en): FIBO currently has three maturity levels: Informative, Provisional, and Release.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
