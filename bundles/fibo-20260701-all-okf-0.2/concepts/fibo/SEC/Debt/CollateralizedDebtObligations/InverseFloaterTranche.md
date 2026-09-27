---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: inverse floater tranche
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/RegularFloaterTranche.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/RegularFloaterTranche
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SuperFloaterTranche.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SuperFloaterTranche
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/FloaterTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/FloaterTranche
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/InverseFloaterTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: inverse floater tranche
type: Ontology Class
---

# inverse floater tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/InverseFloaterTranche>

## Relationships

- **Subclass of**: [FloaterTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/FloaterTranche.md)

## Constraints

- **Disjoint with**: [RegularFloaterTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/RegularFloaterTranche.md)
- **Disjoint with**: [SuperFloaterTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SuperFloaterTranche.md)

## Annotations

- **label** (en): inverse floater tranche

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
