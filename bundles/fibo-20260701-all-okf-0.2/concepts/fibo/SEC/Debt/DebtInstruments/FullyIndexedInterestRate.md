---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fully-indexed interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a variable interest rate that is calculated by adding a margin to a specified index rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Fully indexed interest rates are used for variable rate credit products. The interest rate on a variable (adjustable)
      rate mortgage corresponds to a specific benchmark (often the prime rate, but sometimes LIBOR, the one-year constant-maturity
      Treasury, or other benchmarks) plus a spread (also called the margin. The margin on a fully indexed interest rate product
      is determined by the underwriter and based on the borrower's credit quality.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/BaseRate
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/Margin
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/FloatingInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/FloatingInterestRate
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FullyIndexedInterestRate
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: fully-indexed interest rate
type: Ontology Class
---

# fully-indexed interest rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FullyIndexedInterestRate>

## Definition

a variable interest rate that is calculated by adding a margin to a specified index rate

## Relationships

- **Subclass of**: [FloatingInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/FloatingInterestRate.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: exact qualified cardinality 1 of type [BaseRate](/concepts/fibo/IND/InterestRates/InterestRates/BaseRate.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [Margin](/concepts/fibo/SEC/Debt/DebtInstruments/Margin.md)

## Annotations

- **label**: fully-indexed interest rate
- **definition**: a variable interest rate that is calculated by adding a margin to a specified index rate
- **explanatoryNote**: Fully indexed interest rates are used for variable rate credit products. The interest rate on a variable (adjustable) rate mortgage corresponds to a specific benchmark (often the prime rate, but sometimes LIBOR, the one-year constant-maturity Treasury, or other benchmarks) plus a spread (also called the margin. The margin on a fully indexed interest rate product is determined by the underwriter and based on the borrower's credit quality.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
