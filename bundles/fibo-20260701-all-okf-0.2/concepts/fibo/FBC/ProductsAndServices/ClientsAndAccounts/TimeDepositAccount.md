---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: time deposit account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: deposit account that the depositor does not have a right, and is not permitted, to make withdrawals from within
      six days after the date of deposit unless the deposit is subject to an early withdrawal penalty of at least seven days'
      simple interest on amounts withdrawn within the first six days after deposit
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A time deposit from which partial early withdrawals are permitted must impose additional early withdrawal penalties
      of at least seven days' simple interest on amounts withdrawn within six days after each partial withdrawal. If such
      additional early withdrawal penalties are not imposed, the account ceases to be a time deposit. The account may become
      a savings deposit if it meets the requirements for a savings deposit; otherwise it becomes a demand deposit.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/ContractualProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ContractualProduct
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: time deposit account
type: Ontology Class
---

# time deposit account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount>

## Definition

deposit account that the depositor does not have a right, and is not permitted, to make withdrawals from within six days after the date of deposit unless the deposit is subject to an early withdrawal penalty of at least seven days' simple interest on amounts withdrawn within the first six days after deposit

## Relationships

- **Subclass of**: [NonTransactionDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount.md)
- **Subclass of**: [ContractualProduct](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/ContractualProduct.md)

## Annotations

- **label**: time deposit account
- **definition**: deposit account that the depositor does not have a right, and is not permitted, to make withdrawals from within six days after the date of deposit unless the deposit is subject to an early withdrawal penalty of at least seven days' simple interest on amounts withdrawn within the first six days after deposit
- **explanatoryNote**: A time deposit from which partial early withdrawals are permitted must impose additional early withdrawal penalties of at least seven days' simple interest on amounts withdrawn within six days after each partial withdrawal. If such additional early withdrawal penalties are not imposed, the account ceases to be a time deposit. The account may become a savings deposit if it meets the requirements for a savings deposit; otherwise it becomes a demand deposit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
