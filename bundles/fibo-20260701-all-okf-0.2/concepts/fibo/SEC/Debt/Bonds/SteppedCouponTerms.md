---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: stepped coupon terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: coupon payment terms for securities with a coupon that increases (steps up) while the bond is outstanding
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepSchedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SteppedCouponTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: stepped coupon terms
type: Ontology Class
---

# stepped coupon terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SteppedCouponTerms>

## Definition

coupon payment terms for securities with a coupon that increases (steps up) while the bond is outstanding

## Relationships

- **Subclass of**: [CouponPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md)

## Constraints

- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: some values from of type [StepSchedule](/concepts/fibo/SEC/Debt/DebtInstruments/StepSchedule.md)

## Annotations

- **label**: stepped coupon terms
- **definition**: coupon payment terms for securities with a coupon that increases (steps up) while the bond is outstanding

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
