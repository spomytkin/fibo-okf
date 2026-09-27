---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction record identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: unique identifier for record of transactions
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecordIdentifier
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: transaction record identifier
type: Ontology Class
---

# transaction record identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecordIdentifier>

## Definition

unique identifier for record of transactions

## Relationships

- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [TransactionRecord](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md)

## Annotations

- **label**: transaction record identifier
- **definition**: unique identifier for record of transactions

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
