---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: vanilla option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: common option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via
      a put option) the underlying assets specified at a pre-determined price (i.e., the strike price, fixed or calculated),
      on or before a specified date (the expiration date)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Vanilla options include call or put options that have no special or unusual features, and are typically exchange
      traded.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractDuration
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: vanilla option
type: Ontology Class
---

# vanilla option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption>

## Definition

common option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)

## Relationships

- **Subclass of**: [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)

## Constraints

- **[hasPriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod.md)**: some values from of type [PriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)
- **[hasContractDuration](/concepts/fibo/FND/Agreements/Contracts/hasContractDuration.md)**: some values from of type [ExplicitDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration>)

## Annotations

- **label** (en): vanilla option
- **definition** (en): common option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)
- **explanatoryNote** (en): Vanilla options include call or put options that have no special or unusual features, and are typically exchange traded.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
