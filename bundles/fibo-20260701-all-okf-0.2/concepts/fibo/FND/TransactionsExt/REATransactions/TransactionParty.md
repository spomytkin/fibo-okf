---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction party
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Some entity which takes part in some transaction by receiving and/or parting with some item of economic value or
      some payment or both.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Referred to in REA as Economic Agent (in the context of the economic event, known here as transaction).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/transactsWith
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionParty
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: transaction party
type: Ontology Class
---

# transaction party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionParty>

## Definition

Some entity which takes part in some transaction by receiving and/or parting with some item of economic value or some payment or both.

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[transactsWith](/concepts/fibo/FND/TransactionsExt/REATransactions/transactsWith.md)**: some values from of type [TransactionParty](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md)

## Annotations

- **label** (en): transaction party
- **definition** (en): Some entity which takes part in some transaction by receiving and/or parting with some item of economic value or some payment or both.
- **editorialNote** (en): Referred to in REA as Economic Agent (in the context of the economic event, known here as transaction).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
