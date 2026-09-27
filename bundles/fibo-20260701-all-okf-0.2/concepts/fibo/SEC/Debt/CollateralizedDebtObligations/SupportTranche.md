---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: support tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A tranche which provides payment support to a PAC Tranche.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: PAC tranches have priority over the other tranches in the deal, which are then referred to as the support or companion
      tranches.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PAC-2Class
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SupportTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: support tranche
type: Ontology Class
---

# support tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SupportTranche>

## Definition

A tranche which provides payment support to a PAC Tranche.

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [PAC-2Class](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/PAC-2Class.md)

## Annotations

- **label** (en): support tranche
- **definition** (en): A tranche which provides payment support to a PAC Tranche.
- **explanatoryNote** (en): PAC tranches have priority over the other tranches in the deal, which are then referred to as the support or companion tranches.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
