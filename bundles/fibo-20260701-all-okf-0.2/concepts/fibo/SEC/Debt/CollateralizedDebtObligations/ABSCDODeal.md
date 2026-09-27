---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: a b s c d o deal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An issue of Asset Backed Security CDO notes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: N84b08339a4e94c07966ac336ef3d4d00
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ABSCDODeal
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: a b s c d o deal
type: Ontology Class
---

# a b s c d o deal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ABSCDODeal>

## Definition

An issue of Asset Backed Security CDO notes.

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from value `N84b08339a4e94c07966ac336ef3d4d00`

## Annotations

- **label** (en): a b s c d o deal
- **definition** (en): An issue of Asset Backed Security CDO notes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
