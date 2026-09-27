---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: discharging event
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicCommitment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/terminates
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/LedgerEntry
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/triggers
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/TransactionBusinessEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionBusinessEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/DischargingEvent
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: discharging event
type: Ontology Class
---

# discharging event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/DischargingEvent>

## Relationships

- **Subclass of**: [TransactionBusinessEvent](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionBusinessEvent.md)

## Constraints

- **[terminates](/concepts/fibo/FND/TransactionsExt/REATransactions/terminates.md)**: some values from of type [EconomicCommitment](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicCommitment.md)
- **[triggers](/concepts/fibo/FND/TransactionsExt/REATransactions/triggers.md)**: some values from of type [LedgerEntry](/concepts/fibo/FND/TransactionsExt/REATransactions/LedgerEntry.md)

## Annotations

- **label** (en): discharging event

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
