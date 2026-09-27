---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency forward outright
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: forward contract in a foreign exchange market that locks in the price at which an entity must buy or sell a currency
      on a future date
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The holders of a currency forward are obligated to buy or sell the currency at a specified price, at a specified
      quantity and on a specified future date. These contracts cannot be transferred. Jan 10 Review Notes Outright Forward
      is the term for the professional markets. Spot + Swap where Swap is 2 simultaneous transactions.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: forward outright
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: outright forward currency transaction
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySwap
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyForward.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForward
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForwardOutright
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: currency forward outright
type: Ontology Class
---

# currency forward outright

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForwardOutright>

## Definition

forward contract in a foreign exchange market that locks in the price at which an entity must buy or sell a currency on a future date

## Relationships

- **Subclass of**: [CurrencyForward](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyForward.md)

## Constraints

- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: some values from of type [CurrencySpotContract](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract.md)
- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: some values from of type [CurrencySwap](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencySwap.md)

## Annotations

- **label** (en): currency forward outright
- **definition** (en): forward contract in a foreign exchange market that locks in the price at which an entity must buy or sell a currency on a future date
- **explanatoryNote** (en): The holders of a currency forward are obligated to buy or sell the currency at a specified price, at a specified quantity and on a specified future date. These contracts cannot be transferred. Jan 10 Review Notes Outright Forward is the term for the professional markets. Spot + Swap where Swap is 2 simultaneous transactions.
- **synonym** (en): forward outright
- **synonym** (en): outright forward currency transaction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
