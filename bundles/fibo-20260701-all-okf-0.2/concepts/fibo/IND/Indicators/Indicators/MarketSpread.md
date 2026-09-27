---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market spread
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical measure providing the difference (or spread) between two market rates
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/ScopedMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ScopedMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketSpread
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: market spread
type: Ontology Class
---

# market spread

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketSpread>

## Definition

statistical measure providing the difference (or spread) between two market rates

## Relationships

- **Subclass of**: [ScopedMeasure](/concepts/fibo/FND/Utilities/Analytics/ScopedMeasure.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: exact qualified cardinality 2 of type [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)

## Annotations

- **label**: market spread
- **definition**: statistical measure providing the difference (or spread) between two market rates

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
