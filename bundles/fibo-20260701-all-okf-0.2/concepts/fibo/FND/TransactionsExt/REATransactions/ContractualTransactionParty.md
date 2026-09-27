---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual transaction party
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: That which is party to a transaction which has contractual standing.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In REA, transactions may include those which are not between legal entities,such as for example internal transactions
      within a business and between business units. This term Contractual Transaction Party forms the basis for all party
      definitions for transactions which have some formal contractual basis as being between discrete legal entities (legal
      persons or other contractually capable entities e.g. non incorporated entities). This is the basis for all derivatives
      transactions, securities market transactions and so on.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionParty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransactionParty
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: contractual transaction party
type: Ontology Class
---

# contractual transaction party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransactionParty>

## Definition

That which is party to a transaction which has contractual standing.

## Relationships

- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)
- **Subclass of**: [TransactionParty](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Annotations

- **label** (en): contractual transaction party
- **definition** (en): That which is party to a transaction which has contractual standing.
- **explanatoryNote** (en): In REA, transactions may include those which are not between legal entities,such as for example internal transactions within a business and between business units. This term Contractual Transaction Party forms the basis for all party definitions for transactions which have some formal contractual basis as being between discrete legal entities (legal persons or other contractually capable entities e.g. non incorporated entities). This is the basis for all derivatives transactions, securities market transactions and so on.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
