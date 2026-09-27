---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reinvestment frequency
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: For units where there is Reinvestment distribution, the frequency with which the reinvestment takes place (this
      will be the same or less frequently than the Dividend Payment Frequency), otherwise this fact does not apply.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundReinvestmentPolicy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundReinvestmentPolicy
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/reinvestmentFrequency
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: reinvestment frequency
type: Ontology Property
---

# reinvestment frequency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/reinvestmentFrequency>

## Definition

For units where there is Reinvestment distribution, the frequency with which the reinvestment takes place (this will be the same or less frequently than the Dividend Payment Frequency), otherwise this fact does not apply.

## Relationships

- **Domain**: [FundReinvestmentPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundReinvestmentPolicy.md)
- **Range**: [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)

## Annotations

- **label** (en): reinvestment frequency
- **definition** (en): For units where there is Reinvestment distribution, the frequency with which the reinvestment takes place (this will be the same or less frequently than the Dividend Payment Frequency), otherwise this fact does not apply.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
