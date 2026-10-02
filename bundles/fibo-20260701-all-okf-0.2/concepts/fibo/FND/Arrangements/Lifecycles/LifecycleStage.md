---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lifecycle stage
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: phase in a lifecycle
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: a research and development phase of a product lifecycle, the introduction phase in a marketing lifecycle, a growth
      stage in an economic lifecycle, or the origination phase in the lifecycle of a loan
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
title: lifecycle stage
type: Ontology Class
---

# lifecycle stage

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage>

## Definition

phase in a lifecycle

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[isStageOf](/concepts/fibo/FND/Arrangements/Lifecycles/isStageOf.md)**: some values from of type [Lifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [LifecycleEvent](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleEvent.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [Lifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md)

## Annotations

- **label**: lifecycle stage
- **definition**: phase in a lifecycle
- **example**: a research and development phase of a product lifecycle, the introduction phase in a marketing lifecycle, a growth stage in an economic lifecycle, or the origination phase in the lifecycle of a loan

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
