---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: demand deposit account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: non-interest-bearing deposit account in which deposits are payable immediately on demand, or that are issued with
      an original maturity or required notice period of less than seven days, or that represent funds for which the depository
      institution does not reserve the right to require at least seven days' written notice of an intended withdrawal
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: DDA
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Demand deposits include any matured time deposits without automatic renewal provisions, unless the deposit agreement
      provides for the funds to be transferred at maturity to another type of account. Demand deposits do not include: (i)
      money market deposit accounts (MMDAs) or (ii) NOW accounts.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DemandDepositAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: demand deposit account
type: Ontology Class
---

# demand deposit account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DemandDepositAccount>

## Definition

non-interest-bearing deposit account in which deposits are payable immediately on demand, or that are issued with an original maturity or required notice period of less than seven days, or that represent funds for which the depository institution does not reserve the right to require at least seven days' written notice of an intended withdrawal

## Relationships

- **Subclass of**: [TransactionDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount.md)

## Annotations

- **label**: demand deposit account
- **definition**: non-interest-bearing deposit account in which deposits are payable immediately on demand, or that are issued with an original maturity or required notice period of less than seven days, or that represent funds for which the depository institution does not reserve the right to require at least seven days' written notice of an intended withdrawal
- **abbreviation**: DDA
- **explanatoryNote**: Demand deposits include any matured time deposits without automatic renewal provisions, unless the deposit agreement provides for the funds to be transferred at maturity to another type of account. Demand deposits do not include: (i) money market deposit accounts (MMDAs) or (ii) NOW accounts.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
