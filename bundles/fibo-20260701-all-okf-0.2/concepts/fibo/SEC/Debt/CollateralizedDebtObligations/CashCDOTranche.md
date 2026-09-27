---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cash c d o tranche
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/Tranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/Tranche
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: cash c d o tranche
type: Ontology Class
---

# cash c d o tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche>

## Relationships

- **Subclass of**: [CollateralizedDebtObligation](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)
- **Subclass of**: [Tranche](/concepts/fibo/SEC/Debt/PoolBackedSecurities/Tranche.md)

## Constraints

- **Disjoint with**: [AssetBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)
- **Disjoint with**: [SyntheticCDOTranche](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md)
- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from of type [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Annotations

- **label** (en): cash c d o tranche

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
