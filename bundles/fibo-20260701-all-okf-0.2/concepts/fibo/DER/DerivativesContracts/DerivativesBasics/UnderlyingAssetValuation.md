---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underlying asset valuation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: assessment activity to estimate the value of an underlying asset of a derivative
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasCalculationAgent
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Underlier
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/ValueAssessment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValueAssessment
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UnderlyingAssetValuation
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: underlying asset valuation
type: Ontology Class
---

# underlying asset valuation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UnderlyingAssetValuation>

## Definition

assessment activity to estimate the value of an underlying asset of a derivative

## Relationships

- **Subclass of**: [ValueAssessment](/concepts/fibo/FND/Arrangements/Assessments/ValueAssessment.md)

## Constraints

- **[hasCalculationAgent](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasCalculationAgent.md)**: min qualified cardinality 0 of type [CalculationAgent](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent.md)
- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: some values from of type [Underlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Underlier.md)

## Annotations

- **label** (en): underlying asset valuation
- **definition** (en): assessment activity to estimate the value of an underlying asset of a derivative

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
