---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: seniority
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The seniority which defines this tranche. This is the precedence order for scheduled payments. This is defined
      as Senior, i.e. this is the most senior tranche of the CDO issue.
  domain:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/seniority.2
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: seniority
type: Ontology Property
---

# seniority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/seniority.2>

## Definition

The seniority which defines this tranche. This is the precedence order for scheduled payments. This is defined as Senior, i.e. this is the most senior tranche of the CDO issue.

## Relationships

- **Domain**: [SeniorCDOTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche.md)

## Annotations

- **label** (en): seniority
- **definition** (en): The seniority which defines this tranche. This is the precedence order for scheduled payments. This is defined as Senior, i.e. this is the most senior tranche of the CDO issue.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
