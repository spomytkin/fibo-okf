---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: milestone schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: schedule of milestone events, observations, or other occurrences and the associated dates and/or times when they
      will be done
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MilestoneEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MilestoneSchedule
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: milestone schedule
type: Ontology Class
---

# milestone schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MilestoneSchedule>

## Definition

schedule of milestone events, observations, or other occurrences and the associated dates and/or times when they will be done

## Relationships

- **Subclass of**: [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [MilestoneEvent](/concepts/fibo/FND/Agreements/Contracts/MilestoneEvent.md)

## Annotations

- **label**: milestone schedule
- **definition**: schedule of milestone events, observations, or other occurrences and the associated dates and/or times when they will be done

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
