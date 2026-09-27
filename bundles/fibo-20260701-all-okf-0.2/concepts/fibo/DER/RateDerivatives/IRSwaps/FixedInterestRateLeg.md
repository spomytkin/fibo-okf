---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed interest rate leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: fixed leg that specifies fixed interest amounts and terms for the payment of that interest
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This may be the funding leg of some swaps (i.e. one party agrees to pay fixed interest amounts in exchange for
      whatever is the other leg) or it may be one or both sides of an interest rate swap, where the two parties exchange different
      interest payment streams.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: fixed interest rate payment stream
  disjoint_with:
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/FixedLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedLeg
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedInterestRateLeg
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: fixed interest rate leg
type: Ontology Class
---

# fixed interest rate leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedInterestRateLeg>

## Definition

fixed leg that specifies fixed interest amounts and terms for the payment of that interest

## Relationships

- **Subclass of**: [FixedLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/FixedLeg.md)
- **Subclass of**: [InterestRateSwapLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md)

## Constraints

- **Disjoint with**: [FloatingInterestRateLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg.md)

## Annotations

- **label**: fixed interest rate leg
- **definition**: fixed leg that specifies fixed interest amounts and terms for the payment of that interest
- **explanatoryNote**: This may be the funding leg of some swaps (i.e. one party agrees to pay fixed interest amounts in exchange for whatever is the other leg) or it may be one or both sides of an interest rate swap, where the two parties exchange different interest payment streams.
- **synonym**: fixed interest rate payment stream

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
