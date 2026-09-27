---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is estimate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the measure reflects an estimate (approximation) or not
  domain:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/isEstimate
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: is estimate
type: Ontology Property
---

# is estimate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/isEstimate>

## Definition

indicates whether the measure reflects an estimate (approximation) or not

## Relationships

- **Domain**: [StatisticalMeasure](/concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is estimate
- **definition**: indicates whether the measure reflects an estimate (approximation) or not

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
