---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has best measure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the 'best' (most desirable) possible value for a rating score's hasMeasureWithinScale property
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that hasBestMeasure and hasWorstMeasure may be used together to determine the direction and range of a scale's
      measure values.
  domain:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingScale.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScale
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasBestMeasure
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: has best measure
type: Ontology Property
---

# has best measure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasBestMeasure>

## Definition

indicates the 'best' (most desirable) possible value for a rating score's hasMeasureWithinScale property

## Relationships

- **Domain**: [RatingScale](/concepts/fibo/FND/Arrangements/Ratings/RatingScale.md)
- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: has best measure
- **definition**: indicates the 'best' (most desirable) possible value for a rating score's hasMeasureWithinScale property
- **explanatoryNote**: Note that hasBestMeasure and hasWorstMeasure may be used together to determine the direction and range of a scale's measure values.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
