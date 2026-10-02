---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating scale
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for assigning a value to something according to some scale with respect to quality, a standard, or ranking
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasBestMeasure
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasWorstMeasure
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScalePublisher
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScale
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating scale
type: Ontology Class
---

# rating scale

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScale>

## Definition

system for assigning a value to something according to some scale with respect to quality, a standard, or ranking

## Relationships

- **Subclass of**: [ClassificationScheme](<https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme>)

## Constraints

- **[hasBestMeasure](/concepts/fibo/FND/Arrangements/Ratings/hasBestMeasure.md)**: max qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[hasWorstMeasure](/concepts/fibo/FND/Arrangements/Ratings/hasWorstMeasure.md)**: max qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [RatingScore](/concepts/fibo/FND/Arrangements/Ratings/RatingScore.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: exact qualified cardinality 1 of type [RatingScalePublisher](/concepts/fibo/FND/Arrangements/Ratings/RatingScalePublisher.md)

## Annotations

- **label**: rating scale
- **definition**: system for assigning a value to something according to some scale with respect to quality, a standard, or ranking

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
