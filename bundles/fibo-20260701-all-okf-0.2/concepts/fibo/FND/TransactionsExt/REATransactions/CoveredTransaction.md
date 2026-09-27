---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: covered transaction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A transaction covered by some Master Agreement.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Master Agreement sets out the terms and conditions under which these transactions are to take place between
      the parties. These are Over the Counter transactions, including OTC Derivatives.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MasterAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/ContractualTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransaction
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/CoveredTransaction
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: covered transaction
type: Ontology Class
---

# covered transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/CoveredTransaction>

## Definition

A transaction covered by some Master Agreement.

## Relationships

- **Subclass of**: [ContractualTransaction](/concepts/fibo/FND/TransactionsExt/REATransactions/ContractualTransaction.md)

## Constraints

- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [MasterAgreement](/concepts/fibo/FND/Agreements/Contracts/MasterAgreement.md)

## Annotations

- **label** (en): covered transaction
- **definition** (en): A transaction covered by some Master Agreement.
- **explanatoryNote** (en): The Master Agreement sets out the terms and conditions under which these transactions are to take place between the parties. These are Over the Counter transactions, including OTC Derivatives.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
