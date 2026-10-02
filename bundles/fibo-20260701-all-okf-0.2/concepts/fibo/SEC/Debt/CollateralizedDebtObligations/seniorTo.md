---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: senior to
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Specific kinds of tranche are modeled for example and investigation only and have been removed from the diagrams.
      These will be removed from the final model.
  domain:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MezzanineMBSTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MezzanineMBSTranche
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SeniorMBSTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SeniorMBSTranche
  range:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MezzanineMBSTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MezzanineMBSTranche
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SubordinatedMBSTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SubordinatedMBSTranche
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/cashflowPrecedence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/cashflowPrecedence
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/seniorTo
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: senior to
type: Ontology Property
---

# senior to

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/seniorTo>

## Definition

Specific kinds of tranche are modeled for example and investigation only and have been removed from the diagrams. These will be removed from the final model.

## Relationships

- **Domain**: [MezzanineMBSTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MezzanineMBSTranche.md)
- **Domain**: [SeniorMBSTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SeniorMBSTranche.md)
- **Range**: [MezzanineMBSTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MezzanineMBSTranche.md)
- **Range**: [SubordinatedMBSTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SubordinatedMBSTranche.md)
- **Subproperty of**: [cashflowPrecedence](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/cashflowPrecedence.md)

## Annotations

- **label** (en): senior to
- **definition** (en): Specific kinds of tranche are modeled for example and investigation only and have been removed from the diagrams. These will be removed from the final model.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
