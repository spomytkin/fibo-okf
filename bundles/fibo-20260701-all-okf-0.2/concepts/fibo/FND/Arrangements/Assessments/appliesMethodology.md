---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: applies methodology
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the strategy used for the purposes of determining the fair market or present value of something
  range:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/ValuationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValuationMethod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/appliesMethodology
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: applies methodology
type: Ontology Property
---

# applies methodology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/appliesMethodology>

## Definition

indicates the strategy used for the purposes of determining the fair market or present value of something

## Relationships

- **Range**: [ValuationMethod](/concepts/fibo/FND/Arrangements/Assessments/ValuationMethod.md)
- **Subproperty of**: [hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)

## Annotations

- **label**: applies methodology
- **definition**: indicates the strategy used for the purposes of determining the fair market or present value of something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
