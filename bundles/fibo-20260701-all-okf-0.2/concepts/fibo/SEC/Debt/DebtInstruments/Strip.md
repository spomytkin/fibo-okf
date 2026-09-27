---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: strip
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a tradeable debt instrument created either through the process of removing coupons from a bond and then selling
      the separate parts as a zero coupon bond and an interest paying coupon bond or through taking the opposite position
      from some variant in the options market
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: STRIPS is an acronym for Separate Trading of Registered Interest and Principal of Securities, which has come to
      be used as a term in its own right.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Separate Trading of Registered Interest and Principal of Securities
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FixedIncomeSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/Strip
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: strip
type: Ontology Class
---

# strip

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/Strip>

## Definition

a tradeable debt instrument created either through the process of removing coupons from a bond and then selling the separate parts as a zero coupon bond and an interest paying coupon bond or through taking the opposite position from some variant in the options market

## Relationships

- **Subclass of**: [FixedIncomeSecurity](/concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)

## Annotations

- **label** (en): strip
- **definition** (en): a tradeable debt instrument created either through the process of removing coupons from a bond and then selling the separate parts as a zero coupon bond and an interest paying coupon bond or through taking the opposite position from some variant in the options market
- **explanatoryNote** (en): STRIPS is an acronym for Separate Trading of Registered Interest and Principal of Securities, which has come to be used as a term in its own right.
- **synonym** (en): Separate Trading of Registered Interest and Principal of Securities

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
