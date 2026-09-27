---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction event
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The event component of a transaction
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This describes an event. The event may be delivery of something or settlement of monies in payment for something
      delivered. A Transaction Event will have terms describing the commitment embodied in that side of that transaction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicCommitment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/embodies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEvent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/hasCorresponding
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/DischargingEvent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/hasEnd
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionUndertaking
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/hasStart
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEvent
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: transaction event
type: Ontology Class
---

# transaction event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEvent>

## Definition

The event component of a transaction

## Constraints

- **[embodies](/concepts/fibo/FND/Relations/Relations/embodies.md)**: some values from of type [EconomicCommitment](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicCommitment.md)
- **[hasCorresponding](/concepts/fibo/FND/TransactionsExt/REATransactions/hasCorresponding.md)**: some values from of type [TransactionEvent](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionEvent.md)
- **[hasEnd](/concepts/fibo/FND/TransactionsExt/REATransactions/hasEnd.md)**: some values from of type [DischargingEvent](/concepts/fibo/FND/TransactionsExt/REATransactions/DischargingEvent.md)
- **[hasStart](/concepts/fibo/FND/TransactionsExt/REATransactions/hasStart.md)**: some values from of type [TransactionUndertaking](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionUndertaking.md)

## Annotations

- **label** (en): transaction event
- **definition** (en): The event component of a transaction
- **explanatoryNote** (en): This describes an event. The event may be delivery of something or settlement of monies in payment for something delivered. A Transaction Event will have terms describing the commitment embodied in that side of that transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
