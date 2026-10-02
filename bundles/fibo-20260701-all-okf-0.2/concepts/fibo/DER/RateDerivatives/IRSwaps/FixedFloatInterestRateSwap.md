---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed float interest rate swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest rate swap in which fixed interest payments on the notional are exchanged for floating interest payments
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: fixed-float interest rate swap
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedFloatInterestRateSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: fixed float interest rate swap
type: Ontology Class
---

# fixed float interest rate swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedFloatInterestRateSwap>

## Definition

interest rate swap in which fixed interest payments on the notional are exchanged for floating interest payments

## Relationships

- **Subclass of**: [InterestRateSwap](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)

## Annotations

- **label**: fixed float interest rate swap
- **definition**: interest rate swap in which fixed interest payments on the notional are exchanged for floating interest payments
- **synonym**: fixed-float interest rate swap

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
