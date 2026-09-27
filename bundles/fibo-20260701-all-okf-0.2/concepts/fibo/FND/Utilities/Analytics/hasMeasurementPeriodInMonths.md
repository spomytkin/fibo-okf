---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has measurement period in months
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the coverage period for which the measure is applicable expressed in months
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasMeasurementPeriodInMonths
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has measurement period in months
type: Ontology Property
---

# has measurement period in months

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasMeasurementPeriodInMonths>

## Definition

indicates the coverage period for which the measure is applicable expressed in months

## Relationships

- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label**: has measurement period in months
- **definition**: indicates the coverage period for which the measure is applicable expressed in months

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
