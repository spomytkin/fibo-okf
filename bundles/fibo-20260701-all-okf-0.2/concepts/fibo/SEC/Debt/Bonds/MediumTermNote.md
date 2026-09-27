---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: medium term note
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond issued over time under a shelf registration program, where each issue may have a different coupon and maturity
      typically ranging from one to ten years
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A medium-term note (MTN) is a debt note that usually matures (is paid back) in 5 to 10 years, but the term may
      be less than one year or as long as 100 years. They can be issued on a fixed or floating coupon basis.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: By shelf registration we mean the security registration process where an issuer registers in advance, and can issue
      lots of securities for up to three years.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Medium term notes are typically issued by corporations and financial institutions, although GSEs also have MTN
      programs. MTNs may be issued under a shelf registration program which allows the company to issue bonds over time with
      varying maturities and coupons. Companies issue MTNs to have a more flexible source of funding. They may also issue
      MTN in response to 'reverse inquiry' by investors looking for bonds with specific maturities, issue size and coupon.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MediumTermNote
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: medium term note
type: Ontology Class
---

# medium term note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MediumTermNote>

## Definition

bond issued over time under a shelf registration program, where each issue may have a different coupon and maturity typically ranging from one to ten years

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Annotations

- **label**: medium term note
- **definition**: bond issued over time under a shelf registration program, where each issue may have a different coupon and maturity typically ranging from one to ten years
- **explanatoryNote**: A medium-term note (MTN) is a debt note that usually matures (is paid back) in 5 to 10 years, but the term may be less than one year or as long as 100 years. They can be issued on a fixed or floating coupon basis.
- **explanatoryNote**: By shelf registration we mean the security registration process where an issuer registers in advance, and can issue lots of securities for up to three years.
- **explanatoryNote**: Medium term notes are typically issued by corporations and financial institutions, although GSEs also have MTN programs. MTNs may be issued under a shelf registration program which allows the company to issue bonds over time with varying maturities and coupons. Companies issue MTNs to have a more flexible source of funding. They may also issue MTN in response to 'reverse inquiry' by investors looking for bonds with specific maturities, issue size and coupon.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
