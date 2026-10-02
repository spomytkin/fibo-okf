---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is cash
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Whether the CDO has an underlying pool of real assets. This is yes: the CDO has an underlying pool of real assets,'
  domain:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/isCash.1
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: is cash
type: Ontology Property
---

# is cash

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/isCash.1>

## Definition

Whether the CDO has an underlying pool of real assets. This is yes: the CDO has an underlying pool of real assets,

## Relationships

- **Domain**: [CashCDOTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is cash
- **definition** (en): Whether the CDO has an underlying pool of real assets. This is yes: the CDO has an underlying pool of real assets,

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
