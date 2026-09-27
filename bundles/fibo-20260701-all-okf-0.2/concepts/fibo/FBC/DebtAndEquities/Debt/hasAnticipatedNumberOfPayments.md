---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has anticipated number of payments
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the number of payments promised per the terms of the contract over the lifetime of the contract assuming
      all payments are made
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#positiveInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/hasCount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasCount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasAnticipatedNumberOfPayments
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has anticipated number of payments
type: Ontology Property
---

# has anticipated number of payments

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasAnticipatedNumberOfPayments>

## Definition

specifies the number of payments promised per the terms of the contract over the lifetime of the contract assuming all payments are made

## Relationships

- **Range**: [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)
- **Subproperty of**: [hasCount](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasCount.md)

## Annotations

- **label**: has anticipated number of payments
- **definition**: specifies the number of payments promised per the terms of the contract over the lifetime of the contract assuming all payments are made

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
