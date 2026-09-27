---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: notional step amount
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the amount of money that is subtracted from the notional on each step date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that this is an actual concrete sum of money, which may be specified either as a monetary amount (e.g. dollars
      and cents) or as a percentage of either the original notional amount or the previous notional amount.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNotionalAmount
    value: Nbd2541753a7b4ebd98f6a11817dada50
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepAmount
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: notional step amount
type: Ontology Class
---

# notional step amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepAmount>

## Definition

the amount of money that is subtracted from the notional on each step date

## Relationships

- **Subclass of**: [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)

## Constraints

- **[hasNotionalAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasNotionalAmount.md)**: some values from value `Nbd2541753a7b4ebd98f6a11817dada50`

## Annotations

- **label**: notional step amount
- **definition**: the amount of money that is subtracted from the notional on each step date
- **explanatoryNote**: Note that this is an actual concrete sum of money, which may be specified either as a monetary amount (e.g. dollars and cents) or as a percentage of either the original notional amount or the previous notional amount.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
