---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has floating rate floor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates an optional lower bound on interest rates on floating rate debts
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/FloatingInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/FloatingInterestRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/hasFloatingRateFloor
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: has floating rate floor
type: Ontology Property
---

# has floating rate floor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/hasFloatingRateFloor>

## Definition

indicates an optional lower bound on interest rates on floating rate debts

## Relationships

- **Range**: [FloatingInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/FloatingInterestRate.md)
- **Subproperty of**: [hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)

## Annotations

- **label**: has floating rate floor
- **definition**: indicates an optional lower bound on interest rates on floating rate debts

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
