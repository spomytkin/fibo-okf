---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: key performance indicator
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measurable target that indicates how an individual or business is performing in terms of meeting its goals
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include profits, sales numbers, employee turnover and average annual expenses.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: KPI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.forbes.com/advisor/business/what-is-a-kpi-definition-examples/
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.kpi.org/KPI-Basics/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Although they are both designed to measure performance, KPIs and metrics have different characteristics and are
      used by businesses in different ways. Metrics are measures used to track progress and evaluate success, while KPIs are
      metrics tied to specific goals during a certain period of time. KPIs are designed to align with business goals and targets,
      while metrics evaluate the performance of particular processes.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Key Performance Indicators (KPIs) are the critical (key) quantifiable indicators of progress toward an intended
      result. KPIs provide a focus for strategic and operational improvement, create an analytical basis for decision making
      and help focus attention on what matters most. Managing with the use of KPIs includes setting targets (the desired level
      of performance) and tracking progress against those targets.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasObservedValue
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasTargetValue
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/QualifiedMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/QualifiedMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/KeyPerformanceIndicator
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: key performance indicator
type: Ontology Class
---

# key performance indicator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/KeyPerformanceIndicator>

## Definition

measurable target that indicates how an individual or business is performing in terms of meeting its goals

## Relationships

- **Subclass of**: [QualifiedMeasure](/concepts/fibo/FND/Utilities/Analytics/QualifiedMeasure.md)

## Constraints

- **[hasObservedValue](/concepts/fibo/FND/Utilities/Analytics/hasObservedValue.md)**: min qualified cardinality 0
- **[hasTargetValue](/concepts/fibo/FND/Utilities/Analytics/hasTargetValue.md)**: min qualified cardinality 0

## Annotations

- **label**: key performance indicator
- **definition**: measurable target that indicates how an individual or business is performing in terms of meeting its goals
- **example**: Examples include profits, sales numbers, employee turnover and average annual expenses.
- **abbreviation**: KPI
- **adaptedFrom**: https://www.forbes.com/advisor/business/what-is-a-kpi-definition-examples/
- **adaptedFrom**: https://www.kpi.org/KPI-Basics/
- **explanatoryNote**: Although they are both designed to measure performance, KPIs and metrics have different characteristics and are used by businesses in different ways. Metrics are measures used to track progress and evaluate success, while KPIs are metrics tied to specific goals during a certain period of time. KPIs are designed to align with business goals and targets, while metrics evaluate the performance of particular processes.
- **explanatoryNote**: Key Performance Indicators (KPIs) are the critical (key) quantifiable indicators of progress toward an intended result. KPIs provide a focus for strategic and operational improvement, create an analytical basis for decision making and help focus attention on what matters most. Managing with the use of KPIs includes setting targets (the desired level of performance) and tracking progress against those targets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
