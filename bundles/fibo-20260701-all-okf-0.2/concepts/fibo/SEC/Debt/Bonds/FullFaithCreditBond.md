---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: full faith credit bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond secured by an unconditional promise to pay by another entity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Full faith and credit bonds are typically backed by a government entity and are considered low risk.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: full faith and credit bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/UnsecuredBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UnsecuredBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FullFaithCreditBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: full faith credit bond
type: Ontology Class
---

# full faith credit bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FullFaithCreditBond>

## Definition

bond secured by an unconditional promise to pay by another entity

## Relationships

- **Subclass of**: [UnsecuredBond](/concepts/fibo/SEC/Debt/Bonds/UnsecuredBond.md)

## Annotations

- **label**: full faith credit bond
- **definition**: bond secured by an unconditional promise to pay by another entity
- **explanatoryNote**: Full faith and credit bonds are typically backed by a government entity and are considered low risk.
- **synonym**: full faith and credit bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
