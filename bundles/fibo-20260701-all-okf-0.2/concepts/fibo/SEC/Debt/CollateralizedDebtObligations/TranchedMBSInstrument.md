---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tranched m b s instrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/cashflowPrecedence
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/providesCreditSupportTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/hasNote
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: tranched m b s instrument
type: Ontology Class
---

# tranched m b s instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument>

## Relationships

- **Subclass of**: [MortgageBackedSecurity](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md)

## Constraints

- **[cashflowPrecedence](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/cashflowPrecedence.md)**: all values from of type [TranchedMBSInstrument](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)
- **[providesCreditSupportTo](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/providesCreditSupportTo.md)**: all values from of type [TranchedMBSInstrument](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)
- **[hasNote](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/hasNote.md)**: some values from of type [MBSTrancheNote](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote.md)

## Annotations

- **label** (en): tranched m b s instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
