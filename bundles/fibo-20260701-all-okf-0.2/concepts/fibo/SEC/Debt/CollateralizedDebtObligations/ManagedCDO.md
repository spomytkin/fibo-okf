---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: managed c d o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A CDO where the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the
      portfolio as they see fit.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/StaticCDO.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/StaticCDO
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ManagedManagementStyle
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/managementStyle.1
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ManagedCDOPortfolio
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ManagedCDO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: managed c d o
type: Ontology Class
---

# managed c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ManagedCDO>

## Definition

A CDO where the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **Disjoint with**: [StaticCDO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/StaticCDO.md)
- **[managementStyle.1](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/managementStyle.1.md)**: some values from of type [ManagedManagementStyle](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/ManagedManagementStyle.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [MBSInstrumentSlice](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [ManagedCDOPortfolio](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/ManagedCDOPortfolio.md)

## Annotations

- **label** (en): managed c d o
- **definition** (en): A CDO where the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
