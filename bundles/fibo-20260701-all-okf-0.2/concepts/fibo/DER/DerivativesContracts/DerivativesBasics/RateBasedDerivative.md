---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rate-based derivative
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument where the holder has the right but may not have the obligation, depending on the nature of
      the instrument, to enter into the underlying contract, or pay or receive payment related to the underlying financial
      rate (or rate contract) on a specified future date based on a specified future rate and term
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples of rate-based derivatives include interest rate swaps, forward rate agreements (FRAs), and interest rate
      options such as caps, floors, and collars.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, 2019-10
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Rate-based derivatives derive their value from movements in some rate, e.g, an interest rate, market rate, economic
      indicator, statistical measure calculated over some collection of indices, rather than from traditional assets like
      stocks or commodities. They are commonly used by institutions to manage risks associated with interest rate fluctuations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nde52d22dbceb419e88c36f1a198501a7
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: rate-based derivative
type: Ontology Class
---

# rate-based derivative

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative>

## Definition

derivative instrument where the holder has the right but may not have the obligation, depending on the nature of the instrument, to enter into the underlying contract, or pay or receive payment related to the underlying financial rate (or rate contract) on a specified future date based on a specified future rate and term

## Relationships

- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nde52d22dbceb419e88c36f1a198501a7`

## Annotations

- **label**: rate-based derivative
- **definition**: derivative instrument where the holder has the right but may not have the obligation, depending on the nature of the instrument, to enter into the underlying contract, or pay or receive payment related to the underlying financial rate (or rate contract) on a specified future date based on a specified future rate and term
- **example**: Examples of rate-based derivatives include interest rate swaps, forward rate agreements (FRAs), and interest rate options such as caps, floors, and collars.
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, 2019-10
- **explanatoryNote**: Rate-based derivatives derive their value from movements in some rate, e.g, an interest rate, market rate, economic indicator, statistical measure calculated over some collection of indices, rather than from traditional assets like stocks or commodities. They are commonly used by institutions to manage risks associated with interest rate fluctuations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
