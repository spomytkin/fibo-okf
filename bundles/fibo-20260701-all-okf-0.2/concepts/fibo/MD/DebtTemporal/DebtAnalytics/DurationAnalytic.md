---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: duration analytic
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Weighted average time to receipt of all the payments.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Duration in general is a measure of % price change for a given change in yield. See definition from BMB The duration
      on a traditional bond will be much shorter than the duration relative to the maturity. Duration is the first derivative
      of the curve between Price and Yield. There are multiple types of duration, all of which are variants of this. So Duration
      is the first derivative and the different type of duration measure are different ways of measuring this, for example
      a "quick and dirty" measure of duration or one which.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DurationAnalytic
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: duration analytic
type: Ontology Class
---

# duration analytic

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DurationAnalytic>

## Definition

Weighted average time to receipt of all the payments.

## Relationships

- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Annotations

- **label** (en): duration analytic
- **definition** (en): Weighted average time to receipt of all the payments.
- **editorialNote** (en): Duration in general is a measure of % price change for a given change in yield. See definition from BMB The duration on a traditional bond will be much shorter than the duration relative to the maturity. Duration is the first derivative of the curve between Price and Yield. There are multiple types of duration, all of which are variants of this. So Duration is the first derivative and the different type of duration measure are different ways of measuring this, for example a "quick and dirty" measure of duration or one which.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
