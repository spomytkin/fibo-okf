---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: general ledger
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: organized collection of ledger accounts used to record and summarize changes in position as transactions are posted
      during an accounting period
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Documents/FinancialRecord.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/FinancialRecord
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/GeneralLedger
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: general ledger
type: Ontology Class
---

# general ledger

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/GeneralLedger>

## Definition

organized collection of ledger accounts used to record and summarize changes in position as transactions are posted during an accounting period

## Relationships

- **Subclass of**: [FinancialRecord](/concepts/fibo/FND/Arrangements/Documents/FinancialRecord.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [LedgerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md)

## Annotations

- **label**: general ledger
- **definition**: organized collection of ledger accounts used to record and summarize changes in position as transactions are posted during an accounting period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
