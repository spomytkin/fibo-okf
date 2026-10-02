---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: redemption cycle in business days
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The last business day following the day on which a redemption order is priced (T) by which settlement will be due
      for orders placed with the main Fund Order Desk. Alternatively, if proceeds will be paid following receipt of written
      renunciation, the last business day following receipt of the relevant renunciation documentation by the main Fund Order
      Desk (R) by which the proceeds will be sent.
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/Settlement/SettlementConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementConvention
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/redemptionCycleInBusinessDays
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: redemption cycle in business days
type: Ontology Property
---

# redemption cycle in business days

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/redemptionCycleInBusinessDays>

## Definition

The last business day following the day on which a redemption order is priced (T) by which settlement will be due for orders placed with the main Fund Order Desk. Alternatively, if proceeds will be paid following receipt of written renunciation, the last business day following receipt of the relevant renunciation documentation by the main Fund Order Desk (R) by which the proceeds will be sent.

## Relationships

- **Domain**: [SettlementConvention](/concepts/fibo/FBC/FinancialInstruments/Settlement/SettlementConvention.md)
- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label** (en): redemption cycle in business days
- **definition** (en): The last business day following the day on which a redemption order is priced (T) by which settlement will be due for orders placed with the main Fund Order Desk. Alternatively, if proceeds will be paid following receipt of written renunciation, the last business day following receipt of the relevant renunciation documentation by the main Fund Order Desk (R) by which the proceeds will be sent.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
