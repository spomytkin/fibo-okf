---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has time to maturity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the lifespan of credit agreement or offering, from the date of issuance to the scheduled maturity date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has term to maturity
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasOriginalTimeToMaturity
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has time to maturity
type: Ontology Property
---

# has time to maturity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasOriginalTimeToMaturity>

## Definition

indicates the lifespan of credit agreement or offering, from the date of issuance to the scheduled maturity date

## Relationships

- **Range**: [ExplicitDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration>)
- **Subproperty of**: [hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)

## Annotations

- **label**: has time to maturity
- **definition**: indicates the lifespan of credit agreement or offering, from the date of issuance to the scheduled maturity date
- **synonym**: has term to maturity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
