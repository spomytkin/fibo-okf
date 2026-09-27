---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dividend distribution method
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: convention by which dividends are provided to shareholders
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Distribution may be by payment of a monetary amount or by reinvestment, as specified by the board of directors
      at the time a decision to issue a dividend is made.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/Convention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/Convention
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Strategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Strategy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/DividendDistributionMethod
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: dividend distribution method
type: Ontology Class
---

# dividend distribution method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/DividendDistributionMethod>

## Definition

convention by which dividends are provided to shareholders

## Relationships

- **Subclass of**: [Convention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/Convention.md)
- **Subclass of**: [Strategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Strategy.md)

## Annotations

- **label**: dividend distribution method
- **definition**: convention by which dividends are provided to shareholders
- **explanatoryNote**: Distribution may be by payment of a monetary amount or by reinvestment, as specified by the board of directors at the time a decision to issue a dividend is made.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
