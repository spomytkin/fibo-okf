---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: applies to account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the account to which the transaction record or individual transaction applies
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: applies to account
type: Ontology Property
---

# applies to account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount>

## Definition

indicates the account to which the transaction record or individual transaction applies

## Relationships

- **Range**: [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- **Subproperty of**: [appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)

## Annotations

- **label**: applies to account
- **definition**: indicates the account to which the transaction record or individual transaction applies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
