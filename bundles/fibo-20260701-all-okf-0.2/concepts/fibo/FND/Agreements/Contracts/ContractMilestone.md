---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract milestone
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for an event (milestone), or set of events related to the status or level of completion of a designated
      activity, task, or segment of work required for contract fulfillment
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Milestones are checkpoints that are predefined in the contract, used to measure progress. They specify tasks, deliverables,
      or objectives that must be achieved to meet each milestone and may trigger partial payment.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MilestoneEvent
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ConditionPrecedent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ConditionPrecedent
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractMilestone
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: contract milestone
type: Ontology Class
---

# contract milestone

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractMilestone>

## Definition

classifier for an event (milestone), or set of events related to the status or level of completion of a designated activity, task, or segment of work required for contract fulfillment

## Relationships

- **Subclass of**: [ConditionPrecedent](/concepts/fibo/FND/Agreements/Contracts/ConditionPrecedent.md)
- **Subclass of**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: min qualified cardinality 0 of type [MilestoneEvent](/concepts/fibo/FND/Agreements/Contracts/MilestoneEvent.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Annotations

- **label** (en): contract milestone
- **definition** (en): classifier for an event (milestone), or set of events related to the status or level of completion of a designated activity, task, or segment of work required for contract fulfillment
- **explanatoryNote** (en): Milestones are checkpoints that are predefined in the contract, used to measure progress. They specify tasks, deliverables, or objectives that must be achieved to meet each milestone and may trigger partial payment.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
