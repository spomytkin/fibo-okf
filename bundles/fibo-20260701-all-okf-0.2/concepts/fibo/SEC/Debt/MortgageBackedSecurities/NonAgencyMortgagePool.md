---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non agency mortgage pool
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PoolTrustee
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/hasTrustee
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgagePool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgagePool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: non agency mortgage pool
type: Ontology Class
---

# non agency mortgage pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool>

## Relationships

- **Subclass of**: [MortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgagePool.md)

## Constraints

- **[hasTrustee](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/hasTrustee.md)**: some values from of type [PoolTrustee](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PoolTrustee.md)

## Annotations

- **label** (en): non agency mortgage pool

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
