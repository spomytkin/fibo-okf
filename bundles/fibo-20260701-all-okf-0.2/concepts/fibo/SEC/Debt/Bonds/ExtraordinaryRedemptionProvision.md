---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: extraordinary redemption provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: provision that gives a bond issuer the right to call its bonds due to an unusual one-time occurrence, as specified
      in the offering statement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such redemptions may occur when bond proceeds are not spent according to schedule; when bond proceeds are used
      in a way that makes nontaxable bond interest taxable; or when a catastrophe destroys the project being financed, among
      other reasons.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: extraordinary redemption provision
type: Ontology Class
---

# extraordinary redemption provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision>

## Definition

provision that gives a bond issuer the right to call its bonds due to an unusual one-time occurrence, as specified in the offering statement

## Relationships

- **Subclass of**: [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)

## Annotations

- **label**: extraordinary redemption provision
- **definition**: provision that gives a bond issuer the right to call its bonds due to an unusual one-time occurrence, as specified in the offering statement
- **explanatoryNote**: Such redemptions may occur when bond proceeds are not spent according to schedule; when bond proceeds are used in a way that makes nontaxable bond interest taxable; or when a catastrophe destroys the project being financed, among other reasons.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
