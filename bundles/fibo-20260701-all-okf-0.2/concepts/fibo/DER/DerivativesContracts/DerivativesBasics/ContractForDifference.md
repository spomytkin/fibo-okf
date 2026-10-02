---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract for difference
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cash-settled derivative where the parties agree to exchange on the maturity of the contract the difference between
      the current value of the underlying asset and the initial value of that asset when the contract is initiated
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, suppose the initial price of share XYZ is $100 and a CFD for 1000 shares is exchanged. Both the buyer
      and seller must post some margin. If the price goes to $105, then the buyer gets $5,000 from the seller. If the price
      goes to $95, the buyer pays the seller $5,000. This contract avoids ownership of the stock and all the associated transactions
      issues (like stamp taxes). The contract also allows for leverage (typically 10:1) because the margin that must be posted
      is only a fraction of the value of the underlying asset.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CFD
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.nasdaq.com/glossary/c/contract-for-difference
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These contracts can also be on the difference of two assets' prices. They can also be on the difference of a single
      asset of different maturities (like a bond or futures contracts).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: spread trading
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ContractForDifference
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: contract for difference
type: Ontology Class
---

# contract for difference

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ContractForDifference>

## Definition

cash-settled derivative where the parties agree to exchange on the maturity of the contract the difference between the current value of the underlying asset and the initial value of that asset when the contract is initiated

## Relationships

- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Annotations

- **label** (en): contract for difference
- **definition** (en): cash-settled derivative where the parties agree to exchange on the maturity of the contract the difference between the current value of the underlying asset and the initial value of that asset when the contract is initiated
- **example** (en): For example, suppose the initial price of share XYZ is $100 and a CFD for 1000 shares is exchanged. Both the buyer and seller must post some margin. If the price goes to $105, then the buyer gets $5,000 from the seller. If the price goes to $95, the buyer pays the seller $5,000. This contract avoids ownership of the stock and all the associated transactions issues (like stamp taxes). The contract also allows for leverage (typically 10:1) because the margin that must be posted is only a fraction of the value of the underlying asset.
- **abbreviation** (en): CFD
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
- **adaptedFrom**: https://www.nasdaq.com/glossary/c/contract-for-difference
- **explanatoryNote** (en): These contracts can also be on the difference of two assets' prices. They can also be on the difference of a single asset of different maturities (like a bond or futures contracts).
- **synonym** (en): spread trading

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
