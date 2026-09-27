---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: first regular coupon date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: scheduled date for the first regular coupon payment, in a regular repeating series of coupon periods, after any
      non standard (long or short) first coupon period in the schedule
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FirstRegularCouponDate
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: first regular coupon date
type: Ontology Class
---

# first regular coupon date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FirstRegularCouponDate>

## Definition

scheduled date for the first regular coupon payment, in a regular repeating series of coupon periods, after any non standard (long or short) first coupon period in the schedule

## Relationships

- **Subclass of**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)

## Annotations

- **label**: first regular coupon date
- **definition**: scheduled date for the first regular coupon payment, in a regular repeating series of coupon periods, after any non standard (long or short) first coupon period in the schedule

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
