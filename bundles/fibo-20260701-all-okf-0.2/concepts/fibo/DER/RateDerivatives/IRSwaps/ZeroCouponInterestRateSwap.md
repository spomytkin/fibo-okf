---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: zero coupon interest rate swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest rate swap in which the fixed rate cash flows are compounded and paid once on the expiration date, rather
      than periodically; the payments on the other side (which can be based on a floating interest rate or a fixed rate) follow
      typical swap payment schedules
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNotionalAmount
  subclass_of:
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/ZeroCouponInterestRateSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: zero coupon interest rate swap
type: Ontology Class
---

# zero coupon interest rate swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/ZeroCouponInterestRateSwap>

## Definition

interest rate swap in which the fixed rate cash flows are compounded and paid once on the expiration date, rather than periodically; the payments on the other side (which can be based on a floating interest rate or a fixed rate) follow typical swap payment schedules

## Relationships

- **Subclass of**: [InterestRateSwap](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)

## Constraints

- **[hasNotionalAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasNotionalAmount.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: zero coupon interest rate swap
- **definition**: interest rate swap in which the fixed rate cash flows are compounded and paid once on the expiration date, rather than periodically; the payments on the other side (which can be based on a floating interest rate or a fixed rate) follow typical swap payment schedules
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
