---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed fixed interest rate swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest rate swap in which both parties pay a fixed interest rate that they could not otherwise obtain outside
      of a swap arrangement
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, each counterparty uses a different native currency, but wants to borrow money in the other counterparty's
      native currency.
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Fixed-fixed swaps generally take the form of either a zero coupon swap or a cross-currency swap.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: fixed-fixed interest rate swap
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedInterestRateLeg
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exchanges
  subclass_of:
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedFixedInterestRateSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: fixed fixed interest rate swap
type: Ontology Class
---

# fixed fixed interest rate swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedFixedInterestRateSwap>

## Definition

interest rate swap in which both parties pay a fixed interest rate that they could not otherwise obtain outside of a swap arrangement

## Relationships

- **Subclass of**: [InterestRateSwap](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)

## Constraints

- **[exchanges](/concepts/fibo/FND/Relations/Relations/exchanges.md)**: exact qualified cardinality 2 of type [FixedInterestRateLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/FixedInterestRateLeg.md)

## Annotations

- **label**: fixed fixed interest rate swap
- **definition**: interest rate swap in which both parties pay a fixed interest rate that they could not otherwise obtain outside of a swap arrangement
- **example**: For example, each counterparty uses a different native currency, but wants to borrow money in the other counterparty's native currency.
- **note**: Fixed-fixed swaps generally take the form of either a zero coupon swap or a cross-currency swap.
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10.
- **synonym**: fixed-fixed interest rate swap

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
