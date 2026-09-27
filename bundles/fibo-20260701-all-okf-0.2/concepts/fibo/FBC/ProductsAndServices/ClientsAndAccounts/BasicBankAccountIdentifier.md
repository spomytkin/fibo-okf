---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basic bank account identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier that uniquely identifies an individual account at a specific financial institution in a particular country
      and which includes a bank identifier of the financial institution servicing that account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BBAN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: basic bank account number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BasicBankAccountIdentifier
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: basic bank account identifier
type: Ontology Class
---

# basic bank account identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BasicBankAccountIdentifier>

## Definition

identifier that uniquely identifies an individual account at a specific financial institution in a particular country and which includes a bank identifier of the financial institution servicing that account

## Relationships

- **Subclass of**: [BankAccountIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md)
- **Subclass of**: [StructuredIdentifier](<https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [BankAccountIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [BankIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/BankIdentifier.md)

## Annotations

- **label**: basic bank account identifier
- **definition**: identifier that uniquely identifies an individual account at a specific financial institution in a particular country and which includes a bank identifier of the financial institution servicing that account
- **abbreviation**: BBAN
- **adaptedFrom**: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
- **synonym**: basic bank account number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
