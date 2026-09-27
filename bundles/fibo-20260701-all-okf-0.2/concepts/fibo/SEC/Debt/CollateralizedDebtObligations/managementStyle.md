---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has deal management style
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Whether the CDO is static or managed. This refers to whether or not the CDO manager may make changes to the reference
      portfolio during the life of the security. Further notes: If it is static, collateral is fixed through the life of the
      CDO. The reference assets are bought and then are kept untouched for the term of the product.If it is managed, the reference
      assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.'
  domain:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
  range:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOManagementStyle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOManagementStyle
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/managementStyle
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: has deal management style
type: Ontology Property
---

# has deal management style

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/managementStyle>

## Definition

Whether the CDO is static or managed. This refers to whether or not the CDO manager may make changes to the reference portfolio during the life of the security. Further notes: If it is static, collateral is fixed through the life of the CDO. The reference assets are bought and then are kept untouched for the term of the product.If it is managed, the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

## Relationships

- **Domain**: [CollateralizedDebtObligation](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)
- **Range**: [CDOManagementStyle](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOManagementStyle.md)

## Annotations

- **label** (en): has deal management style
- **definition** (en): Whether the CDO is static or managed. This refers to whether or not the CDO manager may make changes to the reference portfolio during the life of the security. Further notes: If it is static, collateral is fixed through the life of the CDO. The reference assets are bought and then are kept untouched for the term of the product.If it is managed, the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
