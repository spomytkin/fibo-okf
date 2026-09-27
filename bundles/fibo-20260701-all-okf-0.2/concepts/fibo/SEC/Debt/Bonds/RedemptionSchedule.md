---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: redemption schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: repayment schedule whereby a given percentage of a bond issue is redeemed on predefined dates
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/RedemptionEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RedemptionSchedule
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: redemption schedule
type: Ontology Class
---

# redemption schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RedemptionSchedule>

## Definition

repayment schedule whereby a given percentage of a bond issue is redeemed on predefined dates

## Relationships

- **Subclass of**: [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [RedemptionEvent](/concepts/fibo/SEC/Debt/DebtInstruments/RedemptionEvent.md)

## Annotations

- **label**: redemption schedule
- **definition**: repayment schedule whereby a given percentage of a bond issue is redeemed on predefined dates

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
