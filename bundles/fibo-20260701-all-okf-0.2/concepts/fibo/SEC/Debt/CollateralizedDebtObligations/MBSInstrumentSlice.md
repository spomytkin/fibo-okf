---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: m b s instrument slice
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A holding of an individual slice or slices of a tranche.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These may be held in different notes, with different denominations. Tranche slice in this sense is only relevant
      in the context of something like a CDO or analogous things such as CBO.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
    value: N40b78d78a81a469eba27f473f8a8d0e9
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Portfolio
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: m b s instrument slice
type: Ontology Class
---

# m b s instrument slice

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice>

## Definition

A holding of an individual slice or slices of a tranche.

## Relationships

- **Subclass of**: [Portfolio](/concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from value `N40b78d78a81a469eba27f473f8a8d0e9`

## Annotations

- **label** (en): m b s instrument slice
- **definition** (en): A holding of an individual slice or slices of a tranche.
- **explanatoryNote** (en): These may be held in different notes, with different denominations. Tranche slice in this sense is only relevant in the context of something like a CDO or analogous things such as CBO.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
