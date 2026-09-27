---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: remarketable bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate bond program where the coupon rate on outstanding bonds is periodically reset through an auction process
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A remarketing agent (dealer or underwriter) periodically surveys bond holders to identify those who want to sell
      bonds. The agent surveys market (or holds an auction) to determine interest rate at which the bonds can be resold. The
      rate on all outstanding bonds resets at the new rate. These programs are perpetual in the sense they often don't have
      a fixed maturity date, but the company can redeem them. If an auction fails, i.e., the agent can't place all the bonds
      then.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/CorporateBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CorporateBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/FloatingRateNote.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FloatingRateNote
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RemarketableBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: remarketable bond
type: Ontology Class
---

# remarketable bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RemarketableBond>

## Definition

corporate bond program where the coupon rate on outstanding bonds is periodically reset through an auction process

## Relationships

- **Subclass of**: [CorporateBond](/concepts/fibo/SEC/Debt/Bonds/CorporateBond.md)
- **Subclass of**: [FloatingRateNote](/concepts/fibo/SEC/Debt/Bonds/FloatingRateNote.md)

## Annotations

- **label**: remarketable bond
- **definition**: corporate bond program where the coupon rate on outstanding bonds is periodically reset through an auction process
- **explanatoryNote**: A remarketing agent (dealer or underwriter) periodically surveys bond holders to identify those who want to sell bonds. The agent surveys market (or holds an auction) to determine interest rate at which the bonds can be resold. The rate on all outstanding bonds resets at the new rate. These programs are perpetual in the sense they often don't have a fixed maturity date, but the company can redeem them. If an auction fails, i.e., the agent can't place all the bonds then.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
