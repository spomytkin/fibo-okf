---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt pool statistical measure
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: qualified measure of some aspect of the behavior of one or more debt instrument(s) that may vary over time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/QualifiedMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/QualifiedMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: debt pool statistical measure
type: Ontology Class
---

# debt pool statistical measure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure>

## Definition

qualified measure of some aspect of the behavior of one or more debt instrument(s) that may vary over time

## Relationships

- **Subclass of**: [QualifiedMeasure](/concepts/fibo/FND/Utilities/Analytics/QualifiedMeasure.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)
- **[hasApplicablePeriod](<https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod>)**: min qualified cardinality 0 of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label** (en): debt pool statistical measure
- **definition** (en): qualified measure of some aspect of the behavior of one or more debt instrument(s) that may vary over time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
