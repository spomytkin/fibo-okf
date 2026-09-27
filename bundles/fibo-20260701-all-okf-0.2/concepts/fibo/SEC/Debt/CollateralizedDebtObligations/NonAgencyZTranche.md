---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non agency z tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A tranche that does not receive payments while other tranches remain.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'These tranches are credited for interest that would have been received and that interest is accrued to the Z tranche.
      Once all other tranches have been paid, the holders of the Z tranche receive payments. Types of Z Tranche: A Jump Z
      tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the Jump Z tranche
      will begin to receive payments. "Sticky" Jump Z tranches maintain this payment priority until they are retired, while
      regular, non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert
      to their old payment status once the trigger event has passed. Review note: These are currently separate entries - they
      should be entries for types of Z Tranche. Add new list and move these to there.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyZTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: non agency z tranche
type: Ontology Class
---

# non agency z tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyZTranche>

## Definition

A tranche that does not receive payments while other tranches remain.

## Relationships

- **Subclass of**: [TranchedMBSInstrument](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)

## Annotations

- **label** (en): non agency z tranche
- **definition** (en): A tranche that does not receive payments while other tranches remain.
- **editorialNote** (en): These tranches are credited for interest that would have been received and that interest is accrued to the Z tranche. Once all other tranches have been paid, the holders of the Z tranche receive payments. Types of Z Tranche: A Jump Z tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the Jump Z tranche will begin to receive payments. "Sticky" Jump Z tranches maintain this payment priority until they are retired, while regular, non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed. Review note: These are currently separate entries - they should be entries for types of Z Tranche. Add new list and move these to there.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
