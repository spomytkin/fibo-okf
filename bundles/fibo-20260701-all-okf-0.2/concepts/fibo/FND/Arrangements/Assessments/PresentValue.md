---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: present value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: value of an asset today, which may be calculated from reference data and may based on its expected future value
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/QuantitativeValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/QuantitativeValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/PresentValue
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: present value
type: Ontology Class
---

# present value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/PresentValue>

## Definition

value of an asset today, which may be calculated from reference data and may based on its expected future value

## Relationships

- **Subclass of**: [QuantitativeValue](/concepts/fibo/FND/Arrangements/Assessments/QuantitativeValue.md)

## Annotations

- **label**: present value
- **definition**: value of an asset today, which may be calculated from reference data and may based on its expected future value

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
