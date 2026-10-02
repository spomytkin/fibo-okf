---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regular floater tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A floater tranche is a tranche that is keyed to an index and a spread. The spread is added to the index.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For example, 3 month LIBOR +50 -- meaning that the coupon would be whatever the 3 month LIBOR is plus 50 basis
      points. This is not a continuously updated number, rather it resets at specified intervals.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SuperFloaterTranche.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SuperFloaterTranche
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/FloaterTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/FloaterTranche
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/RegularFloaterTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: regular floater tranche
type: Ontology Class
---

# regular floater tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/RegularFloaterTranche>

## Definition

A floater tranche is a tranche that is keyed to an index and a spread. The spread is added to the index.

## Relationships

- **Subclass of**: [FloaterTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/FloaterTranche.md)

## Constraints

- **Disjoint with**: [SuperFloaterTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SuperFloaterTranche.md)

## Annotations

- **label** (en): regular floater tranche
- **definition** (en): A floater tranche is a tranche that is keyed to an index and a spread. The spread is added to the index.
- **explanatoryNote** (en): For example, 3 month LIBOR +50 -- meaning that the coupon would be whatever the 3 month LIBOR is plus 50 basis points. This is not a continuously updated number, rather it resets at specified intervals.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
