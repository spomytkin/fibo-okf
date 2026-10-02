---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is estimated value of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an appraised value to the asset of interest as of the date of the assessment
  domain:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AppraisedValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AppraisedValue
  inverse_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/hasEstimatedValue.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasEstimatedValue
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/isValueOf
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/isEstimatedValueOf
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: is estimated value of
type: Ontology Property
---

# is estimated value of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/isEstimatedValueOf>

## Definition

relates an appraised value to the asset of interest as of the date of the assessment

## Relationships

- **Domain**: [AppraisedValue](/concepts/fibo/FND/Arrangements/Assessments/AppraisedValue.md)
- **Inverse of**: [hasEstimatedValue](/concepts/fibo/FND/Arrangements/Assessments/hasEstimatedValue.md)
- **Subproperty of**: [isValueOf](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/isValueOf>)

## Annotations

- **label**: is estimated value of
- **definition**: relates an appraised value to the asset of interest as of the date of the assessment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
