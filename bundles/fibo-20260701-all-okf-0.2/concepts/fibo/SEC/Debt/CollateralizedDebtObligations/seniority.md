---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: seniority
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'The seniority which defines this tranche. This is the precedence order for scheduled payments. Further notes:
      Tranches are categorized as senior, mezzanine, and subordinated/equity, according to their degree of credit risk. If
      there are defaults or the CDO''s collateral otherwise underperforms, scheduled payments to senior tranches take precedence
      over those of mezzanine tranches, and scheduled payments to mezzanine tranches take precedence over those to subordinated/equity
      tranches. Senior and mezzanine tranches are typically rated, with the former receiving ratings of A to AAA and the latter
      receiving ratings of B to BBB. The ratings reflect both the credit quality of underlying collateral as well as how much
      protection a given tranch is afforded by tranches that are subordinate to it.'
  domain:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
  range:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOTrancheSenioritySelection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOTrancheSenioritySelection
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/seniority
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: seniority
type: Ontology Property
---

# seniority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/seniority>

## Definition

The seniority which defines this tranche. This is the precedence order for scheduled payments. Further notes: Tranches are categorized as senior, mezzanine, and subordinated/equity, according to their degree of credit risk. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior tranches take precedence over those of mezzanine tranches, and scheduled payments to mezzanine tranches take precedence over those to subordinated/equity tranches. Senior and mezzanine tranches are typically rated, with the former receiving ratings of A to AAA and the latter receiving ratings of B to BBB. The ratings reflect both the credit quality of underlying collateral as well as how much protection a given tranch is afforded by tranches that are subordinate to it.

## Relationships

- **Domain**: [CollateralizedDebtObligation](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)
- **Range**: [CDOTrancheSenioritySelection](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOTrancheSenioritySelection.md)

## Annotations

- **label** (en): seniority
- **definition** (en): The seniority which defines this tranche. This is the precedence order for scheduled payments. Further notes: Tranches are categorized as senior, mezzanine, and subordinated/equity, according to their degree of credit risk. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior tranches take precedence over those of mezzanine tranches, and scheduled payments to mezzanine tranches take precedence over those to subordinated/equity tranches. Senior and mezzanine tranches are typically rated, with the former receiving ratings of A to AAA and the latter receiving ratings of B to BBB. The ratings reflect both the credit quality of underlying collateral as well as how much protection a given tranch is afforded by tranches that are subordinate to it.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
