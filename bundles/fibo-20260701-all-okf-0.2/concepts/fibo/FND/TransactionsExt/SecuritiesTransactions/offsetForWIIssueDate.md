---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: offset for w i issue date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Used to calculate actual settlement date from given WI issue date. If issue date is unknwn, this determines how
      many days form the issue date it's going to settle.
  domain:
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/WhenIssuedTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/WhenIssuedTransaction
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/offsetForWIIssueDate
sources:
- id: fibo-source-b8d1f073c7
  resource: references/fibo/FND/TransactionsExt/SecuritiesTransactions.rdf
  sha256: b8d1f073c7f5a249c4aca92393d0d5fbb1100d1d19fc7977632a0f8643da347d
  title: FIBO source FND/TransactionsExt/SecuritiesTransactions.rdf
title: offset for w i issue date
type: Ontology Property
---

# offset for w i issue date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/offsetForWIIssueDate>

## Definition

Used to calculate actual settlement date from given WI issue date. If issue date is unknwn, this determines how many days form the issue date it's going to settle.

## Relationships

- **Domain**: [WhenIssuedTransaction](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/WhenIssuedTransaction.md)
- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label** (en): offset for w i issue date
- **definition** (en): Used to calculate actual settlement date from given WI issue date. If issue date is unknwn, this determines how many days form the issue date it's going to settle.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
