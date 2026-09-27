---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency spot contract
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: foreign-exchange contract for immediate delivery
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Spot rates represent the price that a buyer expects to pay for a foreign currency in another currency at the time
      of the quote. Though the spot exchange rate is said to be settled immediately, the globally accepted settlement cycle
      for foreign-exchange contracts is two days. Foreign-exchange contracts are therefore settled on the second day after
      the day the deal is made.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: foreign exchange spot contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/hasSpotExchangeRate
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/SpotContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/SpotContract
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: currency spot contract
type: Ontology Class
---

# currency spot contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract>

## Definition

foreign-exchange contract for immediate delivery

## Relationships

- **Subclass of**: [CurrencyInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument.md)
- **Subclass of**: [SpotContract](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/SpotContract.md)

## Constraints

- **[hasSpotExchangeRate](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/hasSpotExchangeRate.md)**: some values from of type [QuotedExchangeRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)

## Annotations

- **label** (en): currency spot contract
- **definition** (en): foreign-exchange contract for immediate delivery
- **explanatoryNote** (en): Spot rates represent the price that a buyer expects to pay for a foreign currency in another currency at the time of the quote. Though the spot exchange rate is said to be settled immediately, the globally accepted settlement cycle for foreign-exchange contracts is two days. Foreign-exchange contracts are therefore settled on the second day after the day the deal is made.
- **synonym** (en): foreign exchange spot contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
