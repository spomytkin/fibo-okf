---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partial call
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: call of part of an issue
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallEvent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialCall
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: partial call
type: Ontology Class
---

# partial call

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialCall>

## Definition

call of part of an issue

## Relationships

- **Subclass of**: [CallEvent](/concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md)

## Annotations

- **label**: partial call
- **definition**: call of part of an issue

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
