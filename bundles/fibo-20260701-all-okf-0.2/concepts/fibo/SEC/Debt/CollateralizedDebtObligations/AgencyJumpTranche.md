---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency jump tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A tranche where if there is some sort of trigger event reached then the holders of the tranche will begin to receive
      payments.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/specifiesTrigger
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyCMO
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyJumpTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: agency jump tranche
type: Ontology Class
---

# agency jump tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyJumpTranche>

## Definition

A tranche where if there is some sort of trigger event reached then the holders of the tranche will begin to receive payments.

## Relationships

- **Subclass of**: [AgencyCMO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md)

## Constraints

- **[specifiesTrigger](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/specifiesTrigger.md)**: some values from of type [JumpZTriggerEvent](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent.md)

## Annotations

- **label** (en): agency jump tranche
- **definition** (en): A tranche where if there is some sort of trigger event reached then the holders of the tranche will begin to receive payments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
