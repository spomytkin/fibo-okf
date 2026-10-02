---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: make whole call
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: call allowing the issuer to pay off remaining debt early
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The issuer typically has to make a lump sum payment to the investor(s) derived from a formula based on the net
      present value (NPV) of future coupon payments that will not be paid incrementally because of the call combined with
      the principal payment the investor would have received at maturity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallEvent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MakeWholeCall
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: make whole call
type: Ontology Class
---

# make whole call

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MakeWholeCall>

## Definition

call allowing the issuer to pay off remaining debt early

## Relationships

- **Subclass of**: [CallEvent](/concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md)

## Annotations

- **label**: make whole call
- **definition**: call allowing the issuer to pay off remaining debt early
- **explanatoryNote**: The issuer typically has to make a lump sum payment to the investor(s) derived from a formula based on the net present value (NPV) of future coupon payments that will not be paid incrementally because of the call combined with the principal payment the investor would have received at maturity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
