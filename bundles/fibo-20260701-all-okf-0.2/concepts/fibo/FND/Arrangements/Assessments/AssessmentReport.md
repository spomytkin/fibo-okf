---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: assessment report
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: report that includes an opinion, judgement, appraisal, or view about something and typically the methodology and
      raw inputs used to arrive at that opinion
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Opinion
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/reportsOn
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Reporting/Report.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentReport
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: assessment report
type: Ontology Class
---

# assessment report

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentReport>

## Definition

report that includes an opinion, judgement, appraisal, or view about something and typically the methodology and raw inputs used to arrive at that opinion

## Relationships

- **Subclass of**: [Report](/concepts/fibo/FND/Arrangements/Reporting/Report.md)

## Constraints

- **[reportsOn](/concepts/fibo/FND/Arrangements/Reporting/reportsOn.md)**: min qualified cardinality 0 of type [Opinion](/concepts/fibo/FND/Arrangements/Assessments/Opinion.md)

## Annotations

- **label**: assessment report
- **definition**: report that includes an opinion, judgement, appraisal, or view about something and typically the methodology and raw inputs used to arrive at that opinion

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
