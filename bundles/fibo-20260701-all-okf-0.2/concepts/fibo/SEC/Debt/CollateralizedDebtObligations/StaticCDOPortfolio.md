---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: static c d o portfolio
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A portfolio where collateral of the CDO is fixed through the life of the CDO. The reference assets are bought and
      then are kept untouched for the term of the product.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: There are cases where badly performing assets may be sold off. These are not modeled at present and it's possible
      that a third type of CDO may be indicated where the portfolio manager has certain capabilities.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/StaticCDOPortfolio
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: static c d o portfolio
type: Ontology Class
---

# static c d o portfolio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/StaticCDOPortfolio>

## Definition

A portfolio where collateral of the CDO is fixed through the life of the CDO. The reference assets are bought and then are kept untouched for the term of the product.

## Relationships

- **Subclass of**: [CDOPortfolio](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md)

## Annotations

- **label** (en): static c d o portfolio
- **definition** (en): A portfolio where collateral of the CDO is fixed through the life of the CDO. The reference assets are bought and then are kept untouched for the term of the product.
- **editorialNote** (en): There are cases where badly performing assets may be sold off. These are not modeled at present and it's possible that a third type of CDO may be indicated where the portfolio manager has certain capabilities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
