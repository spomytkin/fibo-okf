---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has payment schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the schedule for fulfillment of an obligation
  range:
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule
sources:
- id: fibo-source-53130861ea
  resource: references/fibo/FND/ProductsAndServices/PaymentsAndSchedules.rdf
  sha256: 53130861eac6d2084e3ddb6496db6123d851e37aa0259feed44cd96fd48920cf
  title: FIBO source FND/ProductsAndServices/PaymentsAndSchedules.rdf
title: has payment schedule
type: Ontology Property
---

# has payment schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule>

## Definition

specifies the schedule for fulfillment of an obligation

## Relationships

- **Range**: [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
- **Subproperty of**: [hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)

## Annotations

- **label**: has payment schedule
- **definition**: specifies the schedule for fulfillment of an obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
