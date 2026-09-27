---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has rate multiplier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a multiplier applied to the coupon before adding the floating rate spread
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/hasRateMultiplier
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: has rate multiplier
type: Ontology Property
---

# has rate multiplier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/hasRateMultiplier>

## Definition

indicates a multiplier applied to the coupon before adding the floating rate spread

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: has rate multiplier
- **definition**: indicates a multiplier applied to the coupon before adding the floating rate spread

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
