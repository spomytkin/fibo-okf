---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: '''Conceptual Framework for Financial Reporting'', September 2024, Financial Accounting Standards Board (FASB).'
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ledger account classifier - liabilities
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for ledger accounts used to track present obligations of an entity to transfer an economic benefit
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Liabilities are obligations whose settlement is expected to involve transferring assets, providing services, or
      other outflows of resources.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Liabilities commonly have features that help identify them. For example, many liabilities require the obligated
      entity to pay cash to one or more identified other entities. Liabilities may not require an entity to pay cash but may
      require the entity to convey other assets, provide services, or transfer other economic benefits or to be ready to do
      so.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: Liabilities
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
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassifier-Liabilities
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: ledger account classifier - liabilities
type: Ontology Individual
---

# ledger account classifier - liabilities

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassifier-Liabilities>

## Definition

classifier for ledger accounts used to track present obligations of an entity to transfer an economic benefit

## Relationships

- **Related to**: [LedgerAccountClassificationScheme](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme.md)
- **Related to**: [LedgerAccountClassificationScheme](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme.md)

## Annotations

- **source**: 'Conceptual Framework for Financial Reporting', September 2024, Financial Accounting Standards Board (FASB).
- **label**: ledger account classifier - liabilities
- **definition**: classifier for ledger accounts used to track present obligations of an entity to transfer an economic benefit
- **explanatoryNote**: Liabilities are obligations whose settlement is expected to involve transferring assets, providing services, or other outflows of resources.
- **explanatoryNote**: Liabilities commonly have features that help identify them. For example, many liabilities require the obligated entity to pay cash to one or more identified other entities. Liabilities may not require an entity to pay cash but may require the entity to convey other assets, provide services, or transfer other economic benefits or to be ready to do so.
- **hasTextValue**: Liabilities

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
