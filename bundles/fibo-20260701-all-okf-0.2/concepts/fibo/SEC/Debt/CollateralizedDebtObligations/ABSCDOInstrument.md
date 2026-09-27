---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: a b s c d o instrument
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: CDO where the underlying asset pool is ABS.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ABSCDOInstrument
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: a b s c d o instrument
type: Ontology Class
---

# a b s c d o instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ABSCDOInstrument>

## Definition

CDO where the underlying asset pool is ABS.

## Relationships

- **Subclass of**: [CashCDOTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md)

## Annotations

- **label** (en): a b s c d o instrument
- **definition** (en): CDO where the underlying asset pool is ABS.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
