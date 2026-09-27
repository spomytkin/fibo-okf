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
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: triggering event
type: Ontology Class
---

# triggering event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent>

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
