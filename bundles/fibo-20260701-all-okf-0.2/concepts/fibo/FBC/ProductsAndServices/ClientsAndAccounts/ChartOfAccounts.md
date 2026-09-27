---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: chart of accounts
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured system of financial account codes used to classify, record, and organize an entity's financial transactions
      in accordance with applicable legal, regulatory, and reporting requirements
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/characterizes
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Documents/FinancialRecord.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/FinancialRecord
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Arrangement
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/ChartOfAccounts
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: chart of accounts
type: Ontology Class
---

# chart of accounts

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/ChartOfAccounts>

## Definition

structured system of financial account codes used to classify, record, and organize an entity's financial transactions in accordance with applicable legal, regulatory, and reporting requirements

## Relationships

- **Subclass of**: [FinancialRecord](/concepts/fibo/FND/Arrangements/Documents/FinancialRecord.md)
- **Subclass of**: [Arrangement](<https://www.omg.org/spec/Commons/Collections/Arrangement>)

## Constraints

- **[characterizes](<https://www.omg.org/spec/Commons/Classifiers/characterizes>)**: some values from of type [LedgerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md)

## Annotations

- **label**: chart of accounts
- **definition**: structured system of financial account codes used to classify, record, and organize an entity's financial transactions in accordance with applicable legal, regulatory, and reporting requirements

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
