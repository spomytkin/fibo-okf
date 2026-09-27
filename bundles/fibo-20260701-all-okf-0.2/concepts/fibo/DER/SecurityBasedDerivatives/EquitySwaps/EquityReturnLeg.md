---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity return leg
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: return leg whose income is based on equities
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nb01f9fce57cc418ca9386fa3701ffb4b
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/ReturnLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityReturnLeg
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: equity return leg
type: Ontology Class
---

# equity return leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityReturnLeg>

## Definition

return leg whose income is based on equities

## Relationships

- **Subclass of**: [ReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/ReturnLeg.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nb01f9fce57cc418ca9386fa3701ffb4b`

## Annotations

- **label** (en): equity return leg
- **definition** (en): return leg whose income is based on equities

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
