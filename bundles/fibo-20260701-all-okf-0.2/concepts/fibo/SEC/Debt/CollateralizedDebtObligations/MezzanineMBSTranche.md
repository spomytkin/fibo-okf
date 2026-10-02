---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mezzanine m b s tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Specific kinds of tranche are modeled for example and investigation only and have been removed from the diagrams.
      These will be removed from the final model.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SubordinatedMBSTranche
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/seniorTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MezzanineMBSTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: mezzanine m b s tranche
type: Ontology Class
---

# mezzanine m b s tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MezzanineMBSTranche>

## Definition

Specific kinds of tranche are modeled for example and investigation only and have been removed from the diagrams. These will be removed from the final model.

## Relationships

- **Subclass of**: [TranchedMBSInstrument](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)

## Constraints

- **[seniorTo](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/seniorTo.md)**: some values from of type [SubordinatedMBSTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SubordinatedMBSTranche.md)

## Annotations

- **label** (en): mezzanine m b s tranche
- **definition** (en): Specific kinds of tranche are modeled for example and investigation only and have been removed from the diagrams. These will be removed from the final model.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
