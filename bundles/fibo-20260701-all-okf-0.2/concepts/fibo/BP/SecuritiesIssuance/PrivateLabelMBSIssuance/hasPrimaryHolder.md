---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has primary holder
  domain:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument
  range:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PrimaryInvestor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PrimaryInvestor
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/hasPrimaryHolder
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: has primary holder
type: Ontology Property
---

# has primary holder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/hasPrimaryHolder>

## Relationships

- **Domain**: [TranchedMBSInstrument](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)
- **Range**: [PrimaryInvestor](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PrimaryInvestor.md)

## Annotations

- **label** (en): has primary holder

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
