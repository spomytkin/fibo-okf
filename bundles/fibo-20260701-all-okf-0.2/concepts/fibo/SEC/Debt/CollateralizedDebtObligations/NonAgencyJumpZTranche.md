---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non agency jump z tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A Jump Z tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the
      Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only
      while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/NonAgencyZTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyZTranche
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpZTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: non agency jump z tranche
type: Ontology Class
---

# non agency jump z tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpZTranche>

## Definition

A Jump Z tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.

## Relationships

- **Subclass of**: [NonAgencyJumpTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche.md)
- **Subclass of**: [NonAgencyZTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/NonAgencyZTranche.md)

## Annotations

- **label** (en): non agency jump z tranche
- **definition** (en): A Jump Z tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
