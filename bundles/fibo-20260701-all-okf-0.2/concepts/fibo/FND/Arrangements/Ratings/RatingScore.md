---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating score
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: grade, classification, or ranking of for something in accordance with some rating scale
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The meaning and methodology for determining a rating score for the rating of something is determined by a rating
      issuer. A given rating may apply at some point in time, as a part of a lifecycle or process, or generally. Typically
      ratings reflect an assessment of a state of affairs at some point in time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasMeasureWithinScale
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScale
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating score
type: Ontology Class
---

# rating score

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore>

## Definition

grade, classification, or ranking of for something in accordance with some rating scale

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[hasMeasureWithinScale](/concepts/fibo/FND/Arrangements/Ratings/hasMeasureWithinScale.md)**: max qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [RatingScale](/concepts/fibo/FND/Arrangements/Ratings/RatingScale.md)

## Annotations

- **label**: rating score
- **definition**: grade, classification, or ranking of for something in accordance with some rating scale
- **explanatoryNote**: The meaning and methodology for determining a rating score for the rating of something is determined by a rating issuer. A given rating may apply at some point in time, as a part of a lifecycle or process, or generally. Typically ratings reflect an assessment of a state of affairs at some point in time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
