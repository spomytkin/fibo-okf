---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has floating rate spread
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: defines the spread rate that can optionally be used to adjust the floating rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such adjustments may be added to or subtracted from the floating rate.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/hasFloatingRateSpread
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: has floating rate spread
type: Ontology Property
---

# has floating rate spread

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/hasFloatingRateSpread>

## Definition

defines the spread rate that can optionally be used to adjust the floating rate

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: has floating rate spread
- **definition**: defines the spread rate that can optionally be used to adjust the floating rate
- **explanatoryNote**: Such adjustments may be added to or subtracted from the floating rate.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
