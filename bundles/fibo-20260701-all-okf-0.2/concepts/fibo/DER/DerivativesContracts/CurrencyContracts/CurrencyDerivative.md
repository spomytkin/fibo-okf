---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency derivative
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another
      currency at an agreed rate of exchange
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FX derivative
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: foreign exchange derivative
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: forex derivative
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasExchangeRateQuotationSource
    value: N67f486ef4e194cfc8293b6dacb146a7f
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: currency derivative
type: Ontology Class
---

# currency derivative

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative>

## Definition

agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency at an agreed rate of exchange

## Relationships

- **Subclass of**: [CurrencyInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument.md)
- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Constraints

- **[hasExchangeRateQuotationSource](/concepts/fibo/IND/ForeignExchange/ForeignExchange/hasExchangeRateQuotationSource.md)**: some values from value `N67f486ef4e194cfc8293b6dacb146a7f`

## Annotations

- **label** (en): currency derivative
- **definition** (en): agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency at an agreed rate of exchange
- **abbreviation** (en): FX derivative
- **synonym** (en): foreign exchange derivative
- **synonym** (en): forex derivative

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
