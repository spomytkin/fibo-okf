---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond coupon
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest rate on a debt security that the issuer promises to pay to the holder until maturity, expressed as an
      annual percentage of the face value
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: coupon percent rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: coupon rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: nominal yield
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondCoupon
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond coupon
type: Ontology Class
---

# bond coupon

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondCoupon>

## Definition

interest rate on a debt security that the issuer promises to pay to the holder until maturity, expressed as an annual percentage of the face value

## Relationships

- **Subclass of**: [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)

## Annotations

- **label**: bond coupon
- **definition**: interest rate on a debt security that the issuer promises to pay to the holder until maturity, expressed as an annual percentage of the face value
- **synonym**: coupon percent rate
- **synonym**: coupon rate
- **synonym**: nominal yield

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
