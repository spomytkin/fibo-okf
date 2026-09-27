---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating assessment event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual assessment resulting in a grade or score and potentially a report describing the score
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingReport
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOutput
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOutput
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAssessmentActivity
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingParty
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAssessmentEvent
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating assessment event
type: Ontology Class
---

# rating assessment event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAssessmentEvent>

## Definition

individual assessment resulting in a grade or score and potentially a report describing the score

## Relationships

- **Subclass of**: [AssessmentEvent](/concepts/fibo/FND/Arrangements/Assessments/AssessmentEvent.md)

## Constraints

- **[hasOutput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOutput.md)**: min qualified cardinality 0 of type [RatingReport](/concepts/fibo/FND/Arrangements/Ratings/RatingReport.md)
- **[hasOutput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOutput.md)**: some values from of type [Rating](/concepts/fibo/FND/Arrangements/Ratings/Rating.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [RatingAssessmentActivity](/concepts/fibo/FND/Arrangements/Ratings/RatingAssessmentActivity.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [RatingParty](/concepts/fibo/FND/Arrangements/Ratings/RatingParty.md)

## Annotations

- **label**: rating assessment event
- **definition**: individual assessment resulting in a grade or score and potentially a report describing the score

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
