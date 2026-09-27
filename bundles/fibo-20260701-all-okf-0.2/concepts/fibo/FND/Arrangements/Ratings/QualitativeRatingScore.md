---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: qualitative rating score
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rating score that is represented as a qualitative code with respect to some rating scale
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Ratings for the creditworthiness of securities are often qualitative, rather than quantitative, such as a triple-A
      (i.e., AAA). Many ratings for products and businesses on the Internet are also qualitative, such as 5-star ratings for
      something.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingScore.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/QualitativeRatingScore
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: qualitative rating score
type: Ontology Class
---

# qualitative rating score

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/QualitativeRatingScore>

## Definition

rating score that is represented as a qualitative code with respect to some rating scale

## Relationships

- **Subclass of**: [RatingScore](/concepts/fibo/FND/Arrangements/Ratings/RatingScore.md)
- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: qualitative rating score
- **definition**: rating score that is represented as a qualitative code with respect to some rating scale
- **explanatoryNote**: Ratings for the creditworthiness of securities are often qualitative, rather than quantitative, such as a triple-A (i.e., AAA). Many ratings for products and businesses on the Internet are also qualitative, such as 5-star ratings for something.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
