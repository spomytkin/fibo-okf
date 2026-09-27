---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: treasury note
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: medium term coupon bearing treasury obligation with original maturity ranging from two to ten years
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MediumTermNote.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MediumTermNote
  - concept: /concepts/fibo/SEC/Debt/Bonds/USTreasurySecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/USTreasurySecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryNote
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: treasury note
type: Ontology Class
---

# treasury note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryNote>

## Definition

medium term coupon bearing treasury obligation with original maturity ranging from two to ten years

## Relationships

- **Subclass of**: [MediumTermNote](/concepts/fibo/SEC/Debt/Bonds/MediumTermNote.md)
- **Subclass of**: [USTreasurySecurity](/concepts/fibo/SEC/Debt/Bonds/USTreasurySecurity.md)

## Annotations

- **label**: treasury note
- **definition**: medium term coupon bearing treasury obligation with original maturity ranging from two to ten years

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
