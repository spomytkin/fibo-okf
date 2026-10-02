---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: senior c d o tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The most senior tranche of the CDO issue. Typically rated A to AAA. If there are defaults or the CDO's collateral
      otherwise underperforms, scheduled payments to senior tranches take precedence over those of mezzanine tranches.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TrancheRatingAtIssue
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ratedAtIssue.1
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/Tranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/Tranche
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: senior c d o tranche
type: Ontology Class
---

# senior c d o tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche>

## Definition

The most senior tranche of the CDO issue. Typically rated A to AAA. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior tranches take precedence over those of mezzanine tranches.

## Relationships

- **Subclass of**: [CollateralizedDebtObligation](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)
- **Subclass of**: [Tranche](/concepts/fibo/SEC/Debt/PoolBackedSecurities/Tranche.md)

## Constraints

- **[ratedAtIssue.1](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/ratedAtIssue.1.md)**: some values from of type [TrancheRatingAtIssue](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TrancheRatingAtIssue.md)

## Annotations

- **label** (en): senior c d o tranche
- **definition** (en): The most senior tranche of the CDO issue. Typically rated A to AAA. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior tranches take precedence over those of mezzanine tranches.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
