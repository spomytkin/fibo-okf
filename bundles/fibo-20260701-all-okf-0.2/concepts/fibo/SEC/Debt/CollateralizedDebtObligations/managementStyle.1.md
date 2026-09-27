---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: management style
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A CDO where the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the
      portfolio as they see fit.
  domain:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
  range:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOManagementStyle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOManagementStyle
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/managementStyle.1
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: management style
type: Ontology Property
---

# management style

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/managementStyle.1>

## Definition

A CDO where the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

## Relationships

- **Domain**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)
- **Range**: [CDOManagementStyle](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOManagementStyle.md)

## Annotations

- **label** (en): management style
- **definition** (en): A CDO where the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
