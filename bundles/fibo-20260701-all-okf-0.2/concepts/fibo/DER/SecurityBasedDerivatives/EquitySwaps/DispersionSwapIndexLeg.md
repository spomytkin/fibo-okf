---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dispersion swap index leg
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dispersion leg whose underlier is an equity index
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N245863219946476b88483baf0406d32c
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/DispersionLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/DispersionSwapIndexLeg
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: dispersion swap index leg
type: Ontology Class
---

# dispersion swap index leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/DispersionSwapIndexLeg>

## Definition

dispersion leg whose underlier is an equity index

## Relationships

- **Subclass of**: [DispersionLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/DispersionLeg.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N245863219946476b88483baf0406d32c`

## Annotations

- **label** (en): dispersion swap index leg
- **definition** (en): dispersion leg whose underlier is an equity index

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
