---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency c m o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Definition for the property ''has tranche type'' which is now a restriction: The type of tranche for the CMO.
      Many different structures are used in practice, including stable PAC bonds or risky IOs and POs. There are floaters
      and inverse floaters. There are also Z-bonds, which are analogous to zero-coupon bonds.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TrancheType
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/hasTrancheType
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyCMO
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/providesPrepaymentSupport
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMBSPool
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/DebtOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyCMO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: agency c m o
type: Ontology Class
---

# agency c m o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyCMO>

## Relationships

- **Subclass of**: [DebtOffering](/concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md)

## Constraints

- **[hasTrancheType](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/hasTrancheType.md)**: some values from of type [TrancheType](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TrancheType.md)
- **[providesPrepaymentSupport](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/providesPrepaymentSupport.md)**: some values from of type [AgencyCMO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [AgencyMBSPool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/AgencyMBSPool.md)

## Annotations

- **label** (en): agency c m o
- **editorialNote** (en): Definition for the property 'has tranche type' which is now a restriction: The type of tranche for the CMO. Many different structures are used in practice, including stable PAC bonds or risky IOs and POs. There are floaters and inverse floaters. There are also Z-bonds, which are analogous to zero-coupon bonds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
