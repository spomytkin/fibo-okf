---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: specifies trigger
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The event which, when it takes place, causes the Jump Z holders to begin receiving payments.
  domain:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyJumpTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyJumpTranche
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche
  range:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/specifiesTrigger
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: specifies trigger
type: Ontology Property
---

# specifies trigger

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/specifiesTrigger>

## Definition

The event which, when it takes place, causes the Jump Z holders to begin receiving payments.

## Relationships

- **Domain**: [AgencyJumpTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyJumpTranche.md)
- **Domain**: [NonAgencyJumpTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche.md)
- **Range**: [JumpZTriggerEvent](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent.md)

## Annotations

- **label** (en): specifies trigger
- **definition** (en): The event which, when it takes place, causes the Jump Z holders to begin receiving payments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
