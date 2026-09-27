---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: perpetual bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond that has no maturity date, i.e., one that pays interest in perpetuity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Perpetual bonds function much like dividend-paying stocks or certain preferred securities. Just as the owner of
      the stock receives a dividend payment as long as the stock is held, the perpetual bond owner receives an interest payment
      as long as the bond is held.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: consul
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PerpetualBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: perpetual bond
type: Ontology Class
---

# perpetual bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PerpetualBond>

## Definition

bond that has no maturity date, i.e., one that pays interest in perpetuity

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Annotations

- **label**: perpetual bond
- **definition**: bond that has no maturity date, i.e., one that pays interest in perpetuity
- **explanatoryNote**: Perpetual bonds function much like dividend-paying stocks or certain preferred securities. Just as the owner of the stock receives a dividend payment as long as the stock is held, the perpetual bond owner receives an interest payment as long as the bond is held.
- **synonym**: consul

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
