---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency spot forward swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'foreign exchange agreement between two parties involving an exchange of two currencies at agreed fixed rates:
      a) on the spot settlement date and b) a reverse exchange on a later specified date'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencySwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySpotForwardSwap
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: currency spot forward swap
type: Ontology Class
---

# currency spot forward swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySpotForwardSwap>

## Definition

foreign exchange agreement between two parties involving an exchange of two currencies at agreed fixed rates: a) on the spot settlement date and b) a reverse exchange on a later specified date

## Relationships

- **Subclass of**: [CurrencySwap](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencySwap.md)

## Constraints

- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: some values from of type [CurrencySpotContract](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract.md)

## Annotations

- **label** (en): currency spot forward swap
- **definition** (en): foreign exchange agreement between two parties involving an exchange of two currencies at agreed fixed rates: a) on the spot settlement date and b) a reverse exchange on a later specified date
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
