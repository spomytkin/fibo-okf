---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has comparison population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the subset of the baseline statistical universe or population used for comparison or analysis
  range:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalUniverse
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasComparisonPopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: has comparison population
type: Ontology Property
---

# has comparison population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasComparisonPopulation>

## Definition

specifies the subset of the baseline statistical universe or population used for comparison or analysis

## Relationships

- **Range**: [StatisticalUniverse](/concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md)
- **Subproperty of**: [hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)

## Annotations

- **label**: has comparison population
- **definition**: specifies the subset of the baseline statistical universe or population used for comparison or analysis

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
