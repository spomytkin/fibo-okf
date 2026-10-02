---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: make whole feature
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a call provision allowing the issuer to pay off remaining debt early
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The issuer typically has to make a lump sum payment to the investor derived from a formula based on the net present
      value (NPV) of future interest or coupon payments that will not be paid incrementally because of the call combined with
      the principal payment the investor would have received at maturity.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: make whole provision
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/MakeWholeFeature
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: make whole feature
type: Ontology Class
---

# make whole feature

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/MakeWholeFeature>

## Definition

a call provision allowing the issuer to pay off remaining debt early

## Relationships

- **Subclass of**: [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)

## Annotations

- **label**: make whole feature
- **definition**: a call provision allowing the issuer to pay off remaining debt early
- **explanatoryNote**: The issuer typically has to make a lump sum payment to the investor derived from a formula based on the net present value (NPV) of future interest or coupon payments that will not be paid incrementally because of the call combined with the principal payment the investor would have received at maturity.
- **synonym**: make whole provision

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
