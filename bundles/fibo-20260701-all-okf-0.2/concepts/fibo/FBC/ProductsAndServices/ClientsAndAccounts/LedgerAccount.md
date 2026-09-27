---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ledger account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual record for one element or sub-element in a ledger that records and summarizes increases, decreases,
      and balances associated with that specific element
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Ledger accounts are internal to a legal entity's accounting system(s).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: ledger account
type: Ontology Class
---

# ledger account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount>

## Definition

individual record for one element or sub-element in a ledger that records and summarizes increases, decreases, and balances associated with that specific element

## Relationships

- **Subclass of**: [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Annotations

- **label**: ledger account
- **definition**: individual record for one element or sub-element in a ledger that records and summarizes increases, decreases, and balances associated with that specific element
- **explanatoryNote**: Ledger accounts are internal to a legal entity's accounting system(s).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
