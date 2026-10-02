---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency forward
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another
      currency, at an agreed date in the future and at an agreed rate of exchange
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: FX forward
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: foreign exchange forward
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/ExchangeRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/hasForwardExchangeRate
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/Forward.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/Forward
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForward
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: currency forward
type: Ontology Class
---

# currency forward

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForward>

## Definition

agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency, at an agreed date in the future and at an agreed rate of exchange

## Relationships

- **Subclass of**: [CurrencyDerivative](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md)
- **Subclass of**: [Forward](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/Forward.md)

## Constraints

- **[hasForwardExchangeRate](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/hasForwardExchangeRate.md)**: some values from of type [ExchangeRate](/concepts/fibo/FND/Accounting/CurrencyAmount/ExchangeRate.md)

## Annotations

- **label** (en): currency forward
- **definition** (en): agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency, at an agreed date in the future and at an agreed rate of exchange
- **synonym** (en): FX forward
- **synonym** (en): foreign exchange forward

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
