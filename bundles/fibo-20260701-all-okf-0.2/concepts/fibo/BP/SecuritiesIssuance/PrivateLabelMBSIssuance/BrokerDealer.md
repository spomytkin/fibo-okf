---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: broker dealer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An entity which may become a primary investor in the issue. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/GetCommitmentFromInvestors
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/commitsTo
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/BrokerDealer
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: broker dealer
type: Ontology Class
---

# broker dealer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/BrokerDealer>

## Definition

An entity which may become a primary investor in the issue. Term origin:MBS PoC Reviews

## Constraints

- **[commitsTo](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/commitsTo.md)**: some values from of type [GetCommitmentFromInvestors](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/GetCommitmentFromInvestors.md)

## Annotations

- **label** (en): broker dealer
- **definition** (en): An entity which may become a primary investor in the issue. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
