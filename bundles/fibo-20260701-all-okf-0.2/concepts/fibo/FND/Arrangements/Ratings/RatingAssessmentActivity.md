---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating assessment activity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: assessment activity resulting in a grade or score and potentially a report describing the score and the process
      used to determine that score
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingParty
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentActivity
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAssessmentActivity
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating assessment activity
type: Ontology Class
---

# rating assessment activity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAssessmentActivity>

## Definition

assessment activity resulting in a grade or score and potentially a report describing the score and the process used to determine that score

## Relationships

- **Subclass of**: [AssessmentActivity](/concepts/fibo/FND/Arrangements/Assessments/AssessmentActivity.md)

## Constraints

- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [RatingParty](/concepts/fibo/FND/Arrangements/Ratings/RatingParty.md)

## Annotations

- **label**: rating assessment activity
- **definition**: assessment activity resulting in a grade or score and potentially a report describing the score and the process used to determine that score

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
