---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tranched m b s deal transaction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The deal transaction by which the MBS Issue is issued to primary investors. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PrimaryInvestor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/hasCounterparty
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSPrimaryDealTransactionSettlementProcess
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/follows
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSDealTransaction
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: tranched m b s deal transaction
type: Ontology Class
---

# tranched m b s deal transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSDealTransaction>

## Definition

The deal transaction by which the MBS Issue is issued to primary investors. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [FinancialPrimaryMarketTransaction](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction.md)

## Constraints

- **[hasCounterparty](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/hasCounterparty.md)**: some values from of type [PrimaryInvestor](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PrimaryInvestor.md)
- **[follows](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/follows.md)**: some values from of type [TranchedMBSPrimaryDealTransactionSettlementProcess](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSPrimaryDealTransactionSettlementProcess.md)

## Annotations

- **label** (en): tranched m b s deal transaction
- **definition** (en): The deal transaction by which the MBS Issue is issued to primary investors. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
