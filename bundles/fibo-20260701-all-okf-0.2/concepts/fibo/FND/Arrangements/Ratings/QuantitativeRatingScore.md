---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: quantitative rating score
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rating score that is a simple numeric value on some scale, such as a credit rating for an individual
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasMeasureWithinScale
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingScore.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/QuantitativeRatingScore
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: quantitative rating score
type: Ontology Class
---

# quantitative rating score

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/QuantitativeRatingScore>

## Definition

rating score that is a simple numeric value on some scale, such as a credit rating for an individual

## Relationships

- **Subclass of**: [RatingScore](/concepts/fibo/FND/Arrangements/Ratings/RatingScore.md)

## Constraints

- **[hasMeasureWithinScale](/concepts/fibo/FND/Arrangements/Ratings/hasMeasureWithinScale.md)**: exact qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: quantitative rating score
- **definition**: rating score that is a simple numeric value on some scale, such as a credit rating for an individual

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
