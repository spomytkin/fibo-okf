---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: estimates value at
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: provides an approximate value of some asset as of some point in time
  range:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AppraisedValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AppraisedValue
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/estimatesValueAt
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: estimates value at
type: Ontology Property
---

# estimates value at

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/estimatesValueAt>

## Definition

provides an approximate value of some asset as of some point in time

## Relationships

- **Range**: [AppraisedValue](/concepts/fibo/FND/Arrangements/Assessments/AppraisedValue.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label**: estimates value at
- **definition**: provides an approximate value of some asset as of some point in time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
