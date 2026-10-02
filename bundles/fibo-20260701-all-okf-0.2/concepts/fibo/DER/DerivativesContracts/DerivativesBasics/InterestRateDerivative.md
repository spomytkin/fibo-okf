---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate derivative
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rate-based derivative whose underlier is an interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, interest rate derivative strategies are the simultaneous trading of two or more rate contracts in
      which two counterparties agree to exchange interest rate cash flows on defined dates during an agreed period, based
      on a specified notional amount, from a fixed rate to a floating rate, floating to fixed, fixed to fixed, or floating
      to floating.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, 2019-10
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nd1d33f36742d4e8d9b5bdd4200b74ff9
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: interest rate derivative
type: Ontology Class
---

# interest rate derivative

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative>

## Definition

rate-based derivative whose underlier is an interest rate

## Relationships

- **Subclass of**: [RateBasedDerivative](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nd1d33f36742d4e8d9b5bdd4200b74ff9`

## Annotations

- **label**: interest rate derivative
- **definition**: rate-based derivative whose underlier is an interest rate
- **example**: For example, interest rate derivative strategies are the simultaneous trading of two or more rate contracts in which two counterparties agree to exchange interest rate cash flows on defined dates during an agreed period, based on a specified notional amount, from a fixed rate to a floating rate, floating to fixed, fixed to fixed, or floating to floating.
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, 2019-10

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
