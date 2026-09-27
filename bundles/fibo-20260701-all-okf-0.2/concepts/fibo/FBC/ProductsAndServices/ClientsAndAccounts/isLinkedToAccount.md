---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is linked to account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: connects a given customer account to another customer account
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/relatesTo.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/relatesTo
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/isLinkedToAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: is linked to account
type: Ontology Property
---

# is linked to account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/isLinkedToAccount>

## Definition

connects a given customer account to another customer account

## Relationships

- **Domain**: [CustomerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
- **Range**: [CustomerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
- **Subproperty of**: [relatesTo](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/relatesTo.md)

## Annotations

- **label**: is linked to account
- **definition**: connects a given customer account to another customer account

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
