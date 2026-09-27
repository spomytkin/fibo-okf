---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has first coupon payment date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the first date on which the issuer or its agent expects or commits to make a coupon payment
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The first coupon date sometimes occurs at an irregular time; that is, if the bond pays coupons every six months,
      the first coupon period may be longer or shorter than six months.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The first coupon payment period can be long or short when this date doesn't coincide with the start of a normal
      coupon payment period.
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFirstCouponPaymentDate
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has first coupon payment date
type: Ontology Property
---

# has first coupon payment date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFirstCouponPaymentDate>

## Definition

specifies the first date on which the issuer or its agent expects or commits to make a coupon payment

## Relationships

- **Domain**: [CouponPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)
- **Subproperty of**: [hasStartDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate>)

## Annotations

- **label**: has first coupon payment date
- **definition**: specifies the first date on which the issuer or its agent expects or commits to make a coupon payment
- **explanatoryNote** (en): The first coupon date sometimes occurs at an irregular time; that is, if the bond pays coupons every six months, the first coupon period may be longer or shorter than six months.
- **explanatoryNote** (en): The first coupon payment period can be long or short when this date doesn't coincide with the start of a normal coupon payment period.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
