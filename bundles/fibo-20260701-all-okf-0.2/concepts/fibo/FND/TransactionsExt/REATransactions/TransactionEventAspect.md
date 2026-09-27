---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction event aspect
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A transaction side as seen from the perspective of one of the parties to the transaction.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This describes one side of one transaction event. The event may be delivery of something or settlement of monies
      in payment for something delivered. A Transaction Event Side shows that side of that transaction from the perspective
      of one or other party.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEventAspect
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/hasCorrespondingAlternativeAspect
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEventAspect
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: transaction event aspect
type: Ontology Class
---

# transaction event aspect

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEventAspect>

## Definition

A transaction side as seen from the perspective of one of the parties to the transaction.

## Constraints

- **[hasCorrespondingAlternativeAspect](/concepts/fibo/FND/TransactionsExt/REATransactions/hasCorrespondingAlternativeAspect.md)**: some values from of type [TransactionEventAspect](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionEventAspect.md)

## Annotations

- **label** (en): transaction event aspect
- **definition** (en): A transaction side as seen from the perspective of one of the parties to the transaction.
- **explanatoryNote** (en): This describes one side of one transaction event. The event may be delivery of something or settlement of monies in payment for something delivered. A Transaction Event Side shows that side of that transaction from the perspective of one or other party.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
