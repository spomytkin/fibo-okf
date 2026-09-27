---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dispersion swap index constituents leg
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dispersion leg whose underlier is a defined set of constituents of a given equity index
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N2413328f8fb449eab26035e787b7c786
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/DispersionLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/DispersionSwapIndexConstituentsLeg
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: dispersion swap index constituents leg
type: Ontology Class
---

# dispersion swap index constituents leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/DispersionSwapIndexConstituentsLeg>

## Definition

dispersion leg whose underlier is a defined set of constituents of a given equity index

## Relationships

- **Subclass of**: [DispersionLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/DispersionLeg.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N2413328f8fb449eab26035e787b7c786`

## Annotations

- **label** (en): dispersion swap index constituents leg
- **definition** (en): dispersion leg whose underlier is a defined set of constituents of a given equity index

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
