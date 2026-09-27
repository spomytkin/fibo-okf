---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: end-of-day market rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: value of a given market rate of the end of the business day for a specific date
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/hasQuotationDateTime
  subclass_of:
  - concept: /concepts/fibo/IND/Indicators/Indicators/MarketRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/EndOfDayMarketRate
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: end-of-day market rate
type: Ontology Class
---

# end-of-day market rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/EndOfDayMarketRate>

## Definition

value of a given market rate of the end of the business day for a specific date

## Relationships

- **Subclass of**: [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)

## Constraints

- **[hasQuotationDateTime](/concepts/fibo/IND/Indicators/Indicators/hasQuotationDateTime.md)**: exact qualified cardinality 1 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: end-of-day market rate
- **definition**: value of a given market rate of the end of the business day for a specific date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
