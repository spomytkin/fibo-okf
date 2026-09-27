---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mezzanine c d o tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The tranche between senior and subordinated. Mezzanine tranches of a CDO issue are typically rated B to BBB.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to mezzanine tranches
      take precedence over those to subordinated/equity tranches.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TrancheRatingAtIssue
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ratedAtIssue
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MezzanineCDOTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: mezzanine c d o tranche
type: Ontology Class
---

# mezzanine c d o tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MezzanineCDOTranche>

## Definition

The tranche between senior and subordinated. Mezzanine tranches of a CDO issue are typically rated B to BBB.

## Relationships

- **Subclass of**: [CollateralizedDebtObligation](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)

## Constraints

- **[ratedAtIssue](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/ratedAtIssue.md)**: some values from of type [TrancheRatingAtIssue](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TrancheRatingAtIssue.md)

## Annotations

- **label** (en): mezzanine c d o tranche
- **definition** (en): The tranche between senior and subordinated. Mezzanine tranches of a CDO issue are typically rated B to BBB.
- **explanatoryNote** (en): If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to mezzanine tranches take precedence over those to subordinated/equity tranches.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
