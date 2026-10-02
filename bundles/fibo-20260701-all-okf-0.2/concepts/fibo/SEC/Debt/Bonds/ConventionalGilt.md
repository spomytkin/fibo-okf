---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: conventional gilt
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: fixed coupon bond issued by HM Treasury that guarantees to pay the holder of the gilt a fixed cash payment (coupon)
      every six months until the maturity date, at which point the holder receives the final coupon payment and the return
      of the principal
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Conventional gilts are the simplest form of government bond and constitute around 75 percent of the gilt portfolio.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.dmo.gov.uk/responsibilities/gilt-market/about-gilts/
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/FixedCouponBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/UKGovernmentSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UKGovernmentSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ConventionalGilt
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: conventional gilt
type: Ontology Class
---

# conventional gilt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ConventionalGilt>

## Definition

fixed coupon bond issued by HM Treasury that guarantees to pay the holder of the gilt a fixed cash payment (coupon) every six months until the maturity date, at which point the holder receives the final coupon payment and the return of the principal

## Relationships

- **See also**: [about-gilts](<https://www.dmo.gov.uk/responsibilities/gilt-market/about-gilts/>)
- **Subclass of**: [FixedCouponBond](/concepts/fibo/SEC/Debt/Bonds/FixedCouponBond.md)
- **Subclass of**: [UKGovernmentSecurity](/concepts/fibo/SEC/Debt/Bonds/UKGovernmentSecurity.md)

## Annotations

- **label**: conventional gilt
- **definition**: fixed coupon bond issued by HM Treasury that guarantees to pay the holder of the gilt a fixed cash payment (coupon) every six months until the maturity date, at which point the holder receives the final coupon payment and the return of the principal
- **explanatoryNote**: Conventional gilts are the simplest form of government bond and constitute around 75 percent of the gilt portfolio.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
