---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: managed c d o portfolio
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A portfolio where the reference assets of the CDO are bought (the portfolio is ramped up) and then the CDO manager
      may alter the portfolio as they see fit.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ManagedCDOPortfolio
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: managed c d o portfolio
type: Ontology Class
---

# managed c d o portfolio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ManagedCDOPortfolio>

## Definition

A portfolio where the reference assets of the CDO are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

## Relationships

- **Subclass of**: [CDOPortfolio](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md)

## Annotations

- **label** (en): managed c d o portfolio
- **definition** (en): A portfolio where the reference assets of the CDO are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
