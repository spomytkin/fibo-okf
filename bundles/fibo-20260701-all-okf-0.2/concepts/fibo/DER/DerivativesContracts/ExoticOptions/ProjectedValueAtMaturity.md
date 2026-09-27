---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: projected value at maturity
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: expected value of the underlying asset at maturity calculated as of some date during the lookback period
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/CalculatedPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CalculatedPrice
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ProjectedValueAtMaturity
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: projected value at maturity
type: Ontology Class
---

# projected value at maturity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ProjectedValueAtMaturity>

## Definition

expected value of the underlying asset at maturity calculated as of some date during the lookback period

## Relationships

- **Subclass of**: [CalculatedPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/CalculatedPrice.md)

## Constraints

- **[hasObservedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime>)**: some values from of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label** (en): projected value at maturity
- **definition** (en): expected value of the underlying asset at maturity calculated as of some date during the lookback period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
