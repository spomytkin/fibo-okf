---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: zero interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an interest rate of zero (0) percent
  - datatype: http://www.w3.org/2001/XMLSchema#decimal
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasRateValue
    value: '0.00'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/FixedInterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroInterestRate
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: zero interest rate
type: Ontology Individual
---

# zero interest rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroInterestRate>

## Definition

an interest rate of zero (0) percent

## Annotations

- **label**: zero interest rate
- **definition**: an interest rate of zero (0) percent
- **hasRateValue**: 0.00

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
