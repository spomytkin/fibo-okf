---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non agency regular jump z tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and
      revert to their old payment status once the trigger event has passed.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEventReversal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/reverts
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpZTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpZTranche
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyRegularJumpZTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: non agency regular jump z tranche
type: Ontology Class
---

# non agency regular jump z tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyRegularJumpZTranche>

## Definition

Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.

## Relationships

- **Subclass of**: [NonAgencyJumpZTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpZTranche.md)

## Constraints

- **[reverts](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/reverts.md)**: some values from of type [JumpZTriggerEventReversal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEventReversal.md)

## Annotations

- **label** (en): non agency regular jump z tranche
- **definition** (en): Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
