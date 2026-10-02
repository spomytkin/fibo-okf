---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: qualified measure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical measure that is constrained by features, quantity kinds or units that refine how it is calculated
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AnchorDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAnchorDate
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/isCalculatedViaMethodology
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/QualifiedMeasure
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: qualified measure
type: Ontology Class
---

# qualified measure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/QualifiedMeasure>

## Definition

statistical measure that is constrained by features, quantity kinds or units that refine how it is calculated

## Relationships

- **Subclass of**: [StatisticalMeasure](/concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md)

## Constraints

- **[hasAnchorDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAnchorDate.md)**: min qualified cardinality 0 of type [AnchorDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/AnchorDate.md)
- **[isCalculatedViaMethodology](/concepts/fibo/FND/Utilities/Analytics/isCalculatedViaMethodology.md)**: min qualified cardinality 0

## Annotations

- **label**: qualified measure
- **definition**: statistical measure that is constrained by features, quantity kinds or units that refine how it is calculated

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
