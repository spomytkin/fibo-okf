---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has interest accrual date offset
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the period in days between each reset date and the commencement of interest accrual for the next period
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/StripStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StripStrategy
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasInterestAccrualDateOffset
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: has interest accrual date offset
type: Ontology Property
---

# has interest accrual date offset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasInterestAccrualDateOffset>

## Definition

indicates the period in days between each reset date and the commencement of interest accrual for the next period

## Relationships

- **Domain**: [StripStrategy](/concepts/fibo/DER/DerivativesContracts/Options/StripStrategy.md)
- **Range**: [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)
- **Subproperty of**: [hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)

## Annotations

- **label** (en): has interest accrual date offset
- **definition** (en): indicates the period in days between each reset date and the commencement of interest accrual for the next period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
