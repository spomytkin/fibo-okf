---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has appraiser
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an assessment or report to an agent that conducts the assessment
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasAppraiser
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: has appraiser
type: Ontology Property
---

# has appraiser

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasAppraiser>

## Definition

relates an assessment or report to an agent that conducts the assessment

## Relationships

- **Subproperty of**: [isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)

## Annotations

- **label**: has appraiser
- **definition**: relates an assessment or report to an agent that conducts the assessment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
