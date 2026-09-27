---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: economic commitment
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Some Commitment which forms part of the subject of some Transaction, being an undertaking by one or other of the
      parties to the transaction, extended to the other party to that same transaction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicAgreement
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/madeBy
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Commitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicCommitment
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: economic commitment
type: Ontology Class
---

# economic commitment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicCommitment>

## Definition

Some Commitment which forms part of the subject of some Transaction, being an undertaking by one or other of the parties to the transaction, extended to the other party to that same transaction.

## Relationships

- **Subclass of**: [Commitment](/concepts/fibo/FND/Agreements/Agreements/Commitment.md)

## Constraints

- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from of type [EconomicAgreement](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicAgreement.md)
- **[madeBy](/concepts/fibo/FND/TransactionsExt/REATransactions/madeBy.md)**: some values from of type [TransactionParty](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md)

## Annotations

- **label** (en): economic commitment
- **definition** (en): Some Commitment which forms part of the subject of some Transaction, being an undertaking by one or other of the parties to the transaction, extended to the other party to that same transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
