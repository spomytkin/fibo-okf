---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has dividend adjustment period
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates at least one date period used to calculate the deviation between an anticipated/expected dividend and
      the actual dividend issued during that period
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/EquityForward.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/EquityForward
  range:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/DividendAdjustmentPeriod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/DividendAdjustmentPeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/hasDividendAdjustmentPeriod
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: has dividend adjustment period
type: Ontology Property
---

# has dividend adjustment period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/hasDividendAdjustmentPeriod>

## Definition

indicates at least one date period used to calculate the deviation between an anticipated/expected dividend and the actual dividend issued during that period

## Relationships

- **Domain**: [EquityForward](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/EquityForward.md)
- **Range**: [DividendAdjustmentPeriod](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/DividendAdjustmentPeriod.md)
- **Subproperty of**: [hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)

## Annotations

- **label** (en): has dividend adjustment period
- **definition** (en): indicates at least one date period used to calculate the deviation between an anticipated/expected dividend and the actual dividend issued during that period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
