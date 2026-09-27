---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: jump z trigger event
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The event which triggers the Jump Z
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If this trigger event is reached then the holders of the Jump Z tranche will begin to receive payments. Regular
      non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their
      old payment status once the trigger event has passed. The event may be a market event or an event relating to the deal.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TriggerEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TriggerEvent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: jump z trigger event
type: Ontology Class
---

# jump z trigger event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent>

## Definition

The event which triggers the Jump Z

## Relationships

- **Subclass of**: [TriggerEvent](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TriggerEvent.md)

## Annotations

- **label** (en): jump z trigger event
- **definition** (en): The event which triggers the Jump Z
- **explanatoryNote** (en): If this trigger event is reached then the holders of the Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed. The event may be a market event or an event relating to the deal.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
