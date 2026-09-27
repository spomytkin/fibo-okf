---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cross-currency interest rate swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest rate swap in which the two streams of interest payments are in different currencies
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/CrossCurrencyInterestRateSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: cross-currency interest rate swap
type: Ontology Class
---

# cross-currency interest rate swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/CrossCurrencyInterestRateSwap>

## Definition

interest rate swap in which the two streams of interest payments are in different currencies

## Relationships

- **Subclass of**: [InterestRateSwap](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)

## Constraints

- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: exact qualified cardinality 2 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: cross-currency interest rate swap
- **definition**: interest rate swap in which the two streams of interest payments are in different currencies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
