---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating report
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: report describing a set of ratings
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/reportsOn
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentReport
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingReport
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating report
type: Ontology Class
---

# rating report

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingReport>

## Definition

report describing a set of ratings

## Relationships

- **Subclass of**: [AssessmentReport](/concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md)

## Constraints

- **[reportsOn](/concepts/fibo/FND/Arrangements/Reporting/reportsOn.md)**: some values from of type [Rating](/concepts/fibo/FND/Arrangements/Ratings/Rating.md)

## Annotations

- **label**: rating report
- **definition**: report describing a set of ratings

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
