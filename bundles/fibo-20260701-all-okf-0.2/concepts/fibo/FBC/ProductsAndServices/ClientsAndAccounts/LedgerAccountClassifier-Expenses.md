---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: '''Conceptual Framework for Financial Reporting'', September 2024, Financial Accounting Standards Board (FASB).'
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ledger account classifier - expenses
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for ledger accounts used to track outflows or other using up of assets of an entity or incurrences of
      its liabilities (or a combination of both) from delivering or producing goods, rendering services, or carrying out other
      activities
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: Expenses
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassifier
  related_to:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassifier-Expenses
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: ledger account classifier - expenses
type: Ontology Individual
---

# ledger account classifier - expenses

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassifier-Expenses>

## Definition

classifier for ledger accounts used to track outflows or other using up of assets of an entity or incurrences of its liabilities (or a combination of both) from delivering or producing goods, rendering services, or carrying out other activities

## Relationships

- **Related to**: [LedgerAccountClassificationScheme](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme.md)
- **Related to**: [LedgerAccountClassificationScheme](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme.md)

## Annotations

- **source**: 'Conceptual Framework for Financial Reporting', September 2024, Financial Accounting Standards Board (FASB).
- **label**: ledger account classifier - expenses
- **definition**: classifier for ledger accounts used to track outflows or other using up of assets of an entity or incurrences of its liabilities (or a combination of both) from delivering or producing goods, rendering services, or carrying out other activities
- **hasTextValue**: Expenses

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
