---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: quantitative value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: value determined via quantitative methods, expressed as a numerical value in appropriate units
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/Value.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Value
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/QuantitativeValue
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: quantitative value
type: Ontology Class
---

# quantitative value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/QuantitativeValue>

## Definition

value determined via quantitative methods, expressed as a numerical value in appropriate units

## Relationships

- **Subclass of**: [Value](/concepts/fibo/FND/Arrangements/Assessments/Value.md)
- **Subclass of**: [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)

## Annotations

- **label**: quantitative value
- **definition**: value determined via quantitative methods, expressed as a numerical value in appropriate units

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
