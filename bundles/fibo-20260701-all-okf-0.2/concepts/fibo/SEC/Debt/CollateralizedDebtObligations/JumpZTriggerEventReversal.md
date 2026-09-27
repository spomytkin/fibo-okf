---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: jump z trigger event reversal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The reversal of the event which triggers the Jump Z
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/specifiesReverseTrigger
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TriggerEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TriggerEvent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEventReversal
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: jump z trigger event reversal
type: Ontology Class
---

# jump z trigger event reversal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEventReversal>

## Definition

The reversal of the event which triggers the Jump Z

## Relationships

- **Subclass of**: [TriggerEvent](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TriggerEvent.md)

## Constraints

- **[specifiesReverseTrigger](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/specifiesReverseTrigger.md)**: some values from of type [JumpZTriggerEvent](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent.md)

## Annotations

- **label** (en): jump z trigger event reversal
- **definition** (en): The reversal of the event which triggers the Jump Z

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
