---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cash c d o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A CDO which has an uderlying portfolio of assets which are held by the issuer.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDO.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDO
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/issues
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashCDO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: cash c d o
type: Ontology Class
---

# cash c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashCDO>

## Definition

A CDO which has an uderlying portfolio of assets which are held by the issuer.

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **Disjoint with**: [SyntheticCDO](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDO.md)
- **[issues](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/issues.md)**: some values from of type [CashCDOTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md)

## Annotations

- **label** (en): cash c d o
- **definition** (en): A CDO which has an uderlying portfolio of assets which are held by the issuer.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
