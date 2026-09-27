---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has starting balance
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an account statement to the amount of money available in that account at the beginning of the statement
      period
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountStatement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountStatement
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Balance
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasStartingBalance
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: has starting balance
type: Ontology Property
---

# has starting balance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasStartingBalance>

## Definition

relates an account statement to the amount of money available in that account at the beginning of the statement period

## Relationships

- **Domain**: [AccountStatement](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountStatement.md)
- **Range**: [Balance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- **Subproperty of**: [hasBalance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance.md)

## Annotations

- **label**: has starting balance
- **definition**: relates an account statement to the amount of money available in that account at the beginning of the statement period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
