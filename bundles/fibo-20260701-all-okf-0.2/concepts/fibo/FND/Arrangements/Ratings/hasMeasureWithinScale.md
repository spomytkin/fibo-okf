---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has measure within scale
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a relative, numeric measure or ordering on a rating scale
  domain:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingScore.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasMeasureWithinScale
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: has measure within scale
type: Ontology Property
---

# has measure within scale

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasMeasureWithinScale>

## Definition

indicates a relative, numeric measure or ordering on a rating scale

## Relationships

- **Domain**: [RatingScore](/concepts/fibo/FND/Arrangements/Ratings/RatingScore.md)
- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: has measure within scale
- **definition**: indicates a relative, numeric measure or ordering on a rating scale

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
