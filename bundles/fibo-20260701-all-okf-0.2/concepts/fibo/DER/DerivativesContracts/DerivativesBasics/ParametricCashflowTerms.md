---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: parametric cashflow terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms for a set of cashflows defined according to a mathematical formula
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CashflowFormula
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasFormula
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CashflowTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CashflowTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ParametricCashflowTerms
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: parametric cashflow terms
type: Ontology Class
---

# parametric cashflow terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ParametricCashflowTerms>

## Definition

terms for a set of cashflows defined according to a mathematical formula

## Relationships

- **Subclass of**: [CashflowTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CashflowTerms.md)

## Constraints

- **[hasFormula](/concepts/fibo/FND/Utilities/Analytics/hasFormula.md)**: some values from of type [CashflowFormula](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CashflowFormula.md)

## Annotations

- **label**: parametric cashflow terms
- **definition**: terms for a set of cashflows defined according to a mathematical formula

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
