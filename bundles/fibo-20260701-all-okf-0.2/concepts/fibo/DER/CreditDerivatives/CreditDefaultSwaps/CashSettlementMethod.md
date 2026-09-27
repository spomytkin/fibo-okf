---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cash settlement method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: strategy for calculating or otherwise establishing a reference final price for the contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The method may include an independently administered synthetic auction process that sets the reference final price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: cash settlement method
type: Ontology Class
---

# cash settlement method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod>

## Definition

strategy for calculating or otherwise establishing a reference final price for the contract

## Relationships

- **Subclass of**: [PriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)

## Annotations

- **label** (en): cash settlement method
- **definition** (en): strategy for calculating or otherwise establishing a reference final price for the contract
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
- **explanatoryNote** (en): The method may include an independently administered synthetic auction process that sets the reference final price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
