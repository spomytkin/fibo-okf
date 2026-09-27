---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: future
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument that obligates the buyer to receive and the seller to deliver the assets specified at an
      agreed price, at some later point in time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A futures contract obligates the buyer to pay the seller a predetermined price based on the market value of the
      underlier, unless the contract is sold before settlement date which may happen if a trader waits to take a profit or
      cut a loss. This contrasts with options trading in which the option buyer may choose whether or not to exercise the
      option. Futures are distinguished from generic forward contracts in that they contain standardized terms, trade on a
      formal exchange, are regulated by overseeing agencies, and are guaranteed by clearing houses. Also, in order to insure
      that payment will occur, futures have a margin requirement that must be settled daily. Finally, by making an offsetting
      trade, taking delivery of goods, or arranging for an exchange of goods, futures contracts can be closed. Hedgers often
      trade futures for the purpose of keeping price risk in check.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: futures contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasLotSize
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Future
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: future
type: Ontology Class
---

# future

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Future>

## Definition

derivative instrument that obligates the buyer to receive and the seller to deliver the assets specified at an agreed price, at some later point in time

## Relationships

- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Constraints

- **[hasLotSize](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasLotSize.md)**: some values from of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: future
- **definition**: derivative instrument that obligates the buyer to receive and the seller to deliver the assets specified at an agreed price, at some later point in time
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10.
- **explanatoryNote** (en): A futures contract obligates the buyer to pay the seller a predetermined price based on the market value of the underlier, unless the contract is sold before settlement date which may happen if a trader waits to take a profit or cut a loss. This contrasts with options trading in which the option buyer may choose whether or not to exercise the option. Futures are distinguished from generic forward contracts in that they contain standardized terms, trade on a formal exchange, are regulated by overseeing agencies, and are guaranteed by clearing houses. Also, in order to insure that payment will occur, futures have a margin requirement that must be settled daily. Finally, by making an offsetting trade, taking delivery of goods, or arranging for an exchange of goods, futures contracts can be closed. Hedgers often trade futures for the purpose of keeping price risk in check.
- **synonym** (en): futures contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
