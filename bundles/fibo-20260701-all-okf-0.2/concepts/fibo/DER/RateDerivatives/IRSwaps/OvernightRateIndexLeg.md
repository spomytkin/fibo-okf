---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: overnight rate index leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: floating leg in which periodic payments are based on an overnight interest rate index multiplied by the same notional
      amount on which the payments for the other leg of the swap are based
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/OvernightRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  subclass_of:
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/OvernightRateIndexLeg
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: overnight rate index leg
type: Ontology Class
---

# overnight rate index leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/OvernightRateIndexLeg>

## Definition

floating leg in which periodic payments are based on an overnight interest rate index multiplied by the same notional amount on which the payments for the other leg of the swap are based

## Relationships

- **Subclass of**: [FloatingInterestRateLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: some values from of type [OvernightRate](/concepts/fibo/IND/InterestRates/InterestRates/OvernightRate.md)

## Annotations

- **label**: overnight rate index leg
- **definition**: floating leg in which periodic payments are based on an overnight interest rate index multiplied by the same notional amount on which the payments for the other leg of the swap are based
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
