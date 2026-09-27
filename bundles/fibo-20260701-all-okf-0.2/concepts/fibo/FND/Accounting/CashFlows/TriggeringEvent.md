---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: triggering event
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event that relates to or triggers some aspect of a credit default swap
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A triggering event is typically a credit event, but could be anything that happens in the marketplace. For example,
      a weather-specific contract could be triggered by a hurricane - which wouldn't be considered a credit event per se.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/TriggeringEvent
sources:
- id: fibo-source-11f30e320a
  resource: references/fibo/FND/Accounting/CashFlows.rdf
  sha256: 11f30e320a47607eb0377d4c97d55d7f8607ad5ba323af00057df476c78573e2
  title: FIBO source FND/Accounting/CashFlows.rdf
title: triggering event
type: Ontology Class
---

# triggering event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/TriggeringEvent>

## Definition

event that relates to or triggers some aspect of a credit default swap

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Annotations

- **label** (en): triggering event
- **definition** (en): event that relates to or triggers some aspect of a credit default swap
- **explanatoryNote** (en): A triggering event is typically a credit event, but could be anything that happens in the marketplace. For example, a weather-specific contract could be triggered by a hurricane - which wouldn't be considered a credit event per se.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
