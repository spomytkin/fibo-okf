---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option whose underlying asset is a group, or basket, of commodities, securities, indices, or currencies
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: As with other options, a basket option gives the holder the right, but not the obligation, to buy or sell the basket
      at a specific price, on or before a certain date. This exotic option has all the characteristics of a standard option,
      but with the basis of the strike price on the weighted value of its components. Currency baskets are the most popular
      type of basket option, and they will settle in the holder's home currency. Because it involves just one transaction,
      a basket option often costs less than multiple single options as it saves on commissions and fees.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nab7a101c8b5a47a5b49ce9881e1f2396
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractDuration
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/BasketOption
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: basket option
type: Ontology Class
---

# basket option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/BasketOption>

## Definition

option whose underlying asset is a group, or basket, of commodities, securities, indices, or currencies

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nab7a101c8b5a47a5b49ce9881e1f2396`
- **[hasPriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod.md)**: some values from of type [PriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)
- **[hasContractDuration](/concepts/fibo/FND/Agreements/Contracts/hasContractDuration.md)**: some values from of type [ExplicitDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration>)

## Annotations

- **label** (en): basket option
- **definition** (en): option whose underlying asset is a group, or basket, of commodities, securities, indices, or currencies
- **explanatoryNote** (en): As with other options, a basket option gives the holder the right, but not the obligation, to buy or sell the basket at a specific price, on or before a certain date. This exotic option has all the characteristics of a standard option, but with the basis of the strike price on the weighted value of its components. Currency baskets are the most popular type of basket option, and they will settle in the holder's home currency. Because it involves just one transaction, a basket option often costs less than multiple single options as it saves on commissions and fees.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
