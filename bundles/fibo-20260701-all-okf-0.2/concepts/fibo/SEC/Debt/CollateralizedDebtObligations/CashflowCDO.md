---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cashflow c d o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A cash-flow CDO is analogous to a CMO. Cash flows from collateral are used to pay principal and interest to investors.
      If such cash flows prove inadequate, principal and interest is paid to tranches according to seniority. At any point
      in time, all immediate obligations to a given tranch are met before any payments are made to less senior tranches.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are some cases where "triggers" can come into effect to cause the payments to be distributed in other ways.
      For example, if the CDO fails its senior overcollateralization (OC) trigger, it may cause extra cash to be diverted
      to the senior tranches' principal in order to bring the deal back into compliance with the OC test.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MarketValueCDO.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MarketValueCDO
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashflowStructure
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/structure.2
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashflowCDO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: cashflow c d o
type: Ontology Class
---

# cashflow c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashflowCDO>

## Definition

A cash-flow CDO is analogous to a CMO. Cash flows from collateral are used to pay principal and interest to investors. If such cash flows prove inadequate, principal and interest is paid to tranches according to seniority. At any point in time, all immediate obligations to a given tranch are met before any payments are made to less senior tranches.

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **Disjoint with**: [MarketValueCDO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MarketValueCDO.md)
- **[structure.2](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/structure.2.md)**: some values from of type [CashflowStructure](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CashflowStructure.md)

## Annotations

- **label** (en): cashflow c d o
- **definition** (en): A cash-flow CDO is analogous to a CMO. Cash flows from collateral are used to pay principal and interest to investors. If such cash flows prove inadequate, principal and interest is paid to tranches according to seniority. At any point in time, all immediate obligations to a given tranch are met before any payments are made to less senior tranches.
- **explanatoryNote** (en): There are some cases where "triggers" can come into effect to cause the payments to be distributed in other ways. For example, if the CDO fails its senior overcollateralization (OC) trigger, it may cause extra cash to be diverted to the senior tranches' principal in order to bring the deal back into compliance with the OC test.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
