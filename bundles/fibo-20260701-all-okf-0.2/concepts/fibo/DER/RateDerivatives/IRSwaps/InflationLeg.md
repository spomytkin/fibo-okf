---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: inflation leg
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: floating rate leg of an inflation swap linked to an inflation index, such as the Consumer Price Index (CPI)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N723c281fc5cb4d798c052c12ca1e3971
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/FloatingLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FloatingLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InflationLeg
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: inflation leg
type: Ontology Class
---

# inflation leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InflationLeg>

## Definition

floating rate leg of an inflation swap linked to an inflation index, such as the Consumer Price Index (CPI)

## Relationships

- **Subclass of**: [FloatingLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/FloatingLeg.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N723c281fc5cb4d798c052c12ca1e3971`

## Annotations

- **label** (en): inflation leg
- **definition** (en): floating rate leg of an inflation swap linked to an inflation index, such as the Consumer Price Index (CPI)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
