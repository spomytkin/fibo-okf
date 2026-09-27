---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction undertaking
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A contractually defined and established commitment to deliver some goods, perform some service or make some payment
      in cash or in kind.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: From REA ontology.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicCommitment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/givesRiseTo
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/UndertakingEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/UndertakingEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionUndertaking
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: transaction undertaking
type: Ontology Class
---

# transaction undertaking

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionUndertaking>

## Definition

A contractually defined and established commitment to deliver some goods, perform some service or make some payment in cash or in kind.

## Relationships

- **Subclass of**: [UndertakingEvent](/concepts/fibo/FND/TransactionsExt/REATransactions/UndertakingEvent.md)

## Constraints

- **[givesRiseTo](/concepts/fibo/FND/TransactionsExt/REATransactions/givesRiseTo.md)**: some values from of type [EconomicCommitment](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicCommitment.md)

## Annotations

- **label** (en): transaction undertaking
- **definition** (en): A contractually defined and established commitment to deliver some goods, perform some service or make some payment in cash or in kind.
- **editorialNote** (en): From REA ontology.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
