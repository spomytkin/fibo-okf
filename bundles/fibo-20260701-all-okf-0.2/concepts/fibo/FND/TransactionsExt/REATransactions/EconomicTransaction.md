---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: economic transaction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Some exchange of some items of economic value between two parties (economic agents).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicResource
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/subject
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicContractTermsSet
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/transactedUnder
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicAgreement
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/transactionEmbodiesEconomicAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicTransaction
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: economic transaction
type: Ontology Class
---

# economic transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicTransaction>

## Definition

Some exchange of some items of economic value between two parties (economic agents).

## Constraints

- **[subject](/concepts/fibo/FND/TransactionsExt/REATransactions/subject.md)**: min qualified cardinality 2 of type [EconomicResource](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicResource.md)
- **[transactedUnder](/concepts/fibo/FND/TransactionsExt/REATransactions/transactedUnder.md)**: some values from of type [EconomicContractTermsSet](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicContractTermsSet.md)
- **[transactionEmbodiesEconomicAgreement](/concepts/fibo/FND/TransactionsExt/REATransactions/transactionEmbodiesEconomicAgreement.md)**: some values from of type [EconomicAgreement](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicAgreement.md)

## Annotations

- **label** (en): economic transaction
- **definition** (en): Some exchange of some items of economic value between two parties (economic agents).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
