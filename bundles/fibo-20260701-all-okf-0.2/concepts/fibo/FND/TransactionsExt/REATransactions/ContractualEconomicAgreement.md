---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual economic agreement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An economic agreement forming part of a transaction, which has contractual standing as evidenced by a contract
      between the two parties to the Agreement.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The REA Economic Agreement may or may not be between two distinct legal persons, as the REA scope includes transactions
      within organizations. For REA based transaction models which are between separate legal entities or persons, the form
      of agreement in force is this Contractual Economic Agreement, that is the agreement, backed by a written or implied
      contract, which is in force between the parties to this agreement.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransactionParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/EconomicAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualEconomicAgreement
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: contractual economic agreement
type: Ontology Class
---

# contractual economic agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualEconomicAgreement>

## Definition

An economic agreement forming part of a transaction, which has contractual standing as evidenced by a contract between the two parties to the Agreement.

## Relationships

- **Subclass of**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **Subclass of**: [EconomicAgreement](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicAgreement.md)

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [ContractualTransactionParty](/concepts/fibo/FND/TransactionsExt/REATransactions/ContractualTransactionParty.md)
- **[confers](/concepts/fibo/FND/Relations/Relations/confers.md)**: some values from of type [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label** (en): contractual economic agreement
- **definition** (en): An economic agreement forming part of a transaction, which has contractual standing as evidenced by a contract between the two parties to the Agreement.
- **explanatoryNote** (en): The REA Economic Agreement may or may not be between two distinct legal persons, as the REA scope includes transactions within organizations. For REA based transaction models which are between separate legal entities or persons, the form of agreement in force is this Contractual Economic Agreement, that is the agreement, backed by a written or implied contract, which is in force between the parties to this agreement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
