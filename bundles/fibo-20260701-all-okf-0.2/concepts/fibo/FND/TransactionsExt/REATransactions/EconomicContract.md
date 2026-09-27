---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: economic contract
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A contract relating to and governing an economic transaction between two parties.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: From REA ontology.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicContractTermsSet
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualEconomicAgreement
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/embodies
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicContract
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: economic contract
type: Ontology Class
---

# economic contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicContract>

## Definition

A contract relating to and governing an economic transaction between two parties.

## Relationships

- **Subclass of**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [EconomicContractTermsSet](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicContractTermsSet.md)
- **[embodies](/concepts/fibo/FND/Relations/Relations/embodies.md)**: some values from of type [ContractualEconomicAgreement](/concepts/fibo/FND/TransactionsExt/REATransactions/ContractualEconomicAgreement.md)

## Annotations

- **label** (en): economic contract
- **definition** (en): A contract relating to and governing an economic transaction between two parties.
- **editorialNote** (en): From REA ontology.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
