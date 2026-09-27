---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has first notional step date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the initial date in a notional step schedule
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/hasFirstNotionalStepDate
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: has first notional step date
type: Ontology Property
---

# has first notional step date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/hasFirstNotionalStepDate>

## Definition

indicates the initial date in a notional step schedule

## Relationships

- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasStartDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate>)

## Annotations

- **label**: has first notional step date
- **definition**: indicates the initial date in a notional step schedule

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
