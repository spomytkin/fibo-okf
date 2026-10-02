---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has reset date offset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the offset from the coupon payment date on which the rate is reset
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariableCouponTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponTerms
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RelativeDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RelativeDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasResetDateOffset
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has reset date offset
type: Ontology Property
---

# has reset date offset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasResetDateOffset>

## Definition

indicates the offset from the coupon payment date on which the rate is reset

## Relationships

- **Domain**: [VariableCouponTerms](/concepts/fibo/SEC/Debt/Bonds/VariableCouponTerms.md)
- **Range**: [RelativeDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RelativeDate.md)
- **Subproperty of**: [hasDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDate>)

## Annotations

- **label**: has reset date offset
- **definition**: indicates the offset from the coupon payment date on which the rate is reset

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
