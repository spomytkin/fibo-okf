---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: '''Conceptual Framework for Financial Reporting'', September 2024, Financial Accounting Standards Board (FASB).'
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ledger account classifier - assets
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for ledger accounts used to track present rights of an entity to an economic benefit
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A present right of an entity to an economic benefit entitles the entity to the economic benefit and the ability
      to restrict others' access to the benefit to which the entity is entitled. Assets are economic resources that an entity
      controls as a result of past events and that it expects to generate future economic benefits.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Assets commonly have features that help identify them - for example, assets may be contractual, tangible, exchangeable,
      or separable. However, those features are not essential characteristics of assets. Their absence is not sufficient to
      preclude an item from qualifying as an asset.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: Assets
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
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassifier-Assets
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: ledger account classifier - assets
type: Ontology Individual
---

# ledger account classifier - assets

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassifier-Assets>

## Definition

classifier for ledger accounts used to track present rights of an entity to an economic benefit

## Relationships

- **Related to**: [LedgerAccountClassificationScheme](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme.md)
- **Related to**: [LedgerAccountClassificationScheme](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccountClassificationScheme.md)

## Annotations

- **source**: 'Conceptual Framework for Financial Reporting', September 2024, Financial Accounting Standards Board (FASB).
- **label**: ledger account classifier - assets
- **definition**: classifier for ledger accounts used to track present rights of an entity to an economic benefit
- **explanatoryNote**: A present right of an entity to an economic benefit entitles the entity to the economic benefit and the ability to restrict others' access to the benefit to which the entity is entitled. Assets are economic resources that an entity controls as a result of past events and that it expects to generate future economic benefits.
- **explanatoryNote**: Assets commonly have features that help identify them - for example, assets may be contractual, tangible, exchangeable, or separable. However, those features are not essential characteristics of assets. Their absence is not sufficient to preclude an item from qualifying as an asset.
- **hasTextValue**: Assets

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
