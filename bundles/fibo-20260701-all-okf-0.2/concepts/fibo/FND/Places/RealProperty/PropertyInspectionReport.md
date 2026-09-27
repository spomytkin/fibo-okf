---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: property inspection report
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: report covering the findings of a property inspection
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentReport
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PropertyInspectionReport
sources:
- id: fibo-source-f0e5ecd06c
  resource: references/fibo/FND/Places/RealProperty.rdf
  sha256: f0e5ecd06c164d1e5fff0c1236869b2014bcba3d7008365dcc2c7363064202bd
  title: FIBO source FND/Places/RealProperty.rdf
title: property inspection report
type: Ontology Class
---

# property inspection report

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PropertyInspectionReport>

## Definition

report covering the findings of a property inspection

## Relationships

- **Subclass of**: [AssessmentReport](/concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md)

## Constraints

- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [RealProperty](/concepts/fibo/FND/Places/RealProperty/RealProperty.md)

## Annotations

- **label**: property inspection report
- **definition**: report covering the findings of a property inspection

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
