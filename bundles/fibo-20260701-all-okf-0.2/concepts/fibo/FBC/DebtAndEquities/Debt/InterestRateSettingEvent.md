---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate setting event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event on which an initial rate for a given contract is set, which may be relative the the occurrence of some other
      contract lifecycle event, such as the execution date
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/InterestCalculation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestCalculation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateSettingEvent
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: interest rate setting event
type: Ontology Class
---

# interest rate setting event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateSettingEvent>

## Definition

event on which an initial rate for a given contract is set, which may be relative the the occurrence of some other contract lifecycle event, such as the execution date

## Relationships

- **Subclass of**: [InterestCalculation](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestCalculation.md)

## Annotations

- **label**: interest rate setting event
- **definition**: event on which an initial rate for a given contract is set, which may be relative the the occurrence of some other contract lifecycle event, such as the execution date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
