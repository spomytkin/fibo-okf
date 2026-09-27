---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: account identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier that denotes an account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: account number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: account identifier
type: Ontology Class
---

# account identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier>

## Definition

identifier that denotes an account

## Relationships

- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Annotations

- **label**: account identifier
- **definition**: identifier that denotes an account
- **adaptedFrom**: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
- **synonym**: account number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
