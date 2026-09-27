---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bank account identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier that identifies a demand deposit account provided by a bank
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bank account number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DemandDepositAccount
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: bank account identifier
type: Ontology Class
---

# bank account identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier>

## Definition

identifier that identifies a demand deposit account provided by a bank

## Relationships

- **Subclass of**: [AccountIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [DemandDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/DemandDepositAccount.md)

## Annotations

- **label**: bank account identifier
- **definition**: identifier that identifies a demand deposit account provided by a bank
- **adaptedFrom**: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
- **synonym**: bank account number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
