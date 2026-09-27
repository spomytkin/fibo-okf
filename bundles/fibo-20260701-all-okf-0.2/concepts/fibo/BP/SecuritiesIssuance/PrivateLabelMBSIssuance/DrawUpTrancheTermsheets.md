---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: draw up tranche termsheets
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/requires
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/DrawUpTrancheTermsheets
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: draw up tranche termsheets
type: Ontology Class
---

# draw up tranche termsheets

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/DrawUpTrancheTermsheets>

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md)

## Constraints

- **[requires](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/requires.md)**: some values from of type [NonAgencyMortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool.md)

## Annotations

- **label** (en): draw up tranche termsheets

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
