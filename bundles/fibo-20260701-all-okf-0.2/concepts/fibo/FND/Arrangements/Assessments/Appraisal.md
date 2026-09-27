---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: appraisal
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: written estimate of the market value of something as of some point in time, typically provided by a qualified appraiser
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AppraisedValue
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/estimatesValueAt
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraiser
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isGeneratedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentReport
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: appraisal
type: Ontology Class
---

# appraisal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal>

## Definition

written estimate of the market value of something as of some point in time, typically provided by a qualified appraiser

## Relationships

- **Subclass of**: [AssessmentReport](/concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md)

## Constraints

- **[estimatesValueAt](/concepts/fibo/FND/Arrangements/Assessments/estimatesValueAt.md)**: some values from of type [AppraisedValue](/concepts/fibo/FND/Arrangements/Assessments/AppraisedValue.md)
- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: min qualified cardinality 0 of type [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **[isGeneratedBy](/concepts/fibo/FND/Relations/Relations/isGeneratedBy.md)**: min qualified cardinality 0 of type [Appraiser](/concepts/fibo/FND/Arrangements/Assessments/Appraiser.md)

## Annotations

- **label**: appraisal
- **definition**: written estimate of the market value of something as of some point in time, typically provided by a qualified appraiser

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
