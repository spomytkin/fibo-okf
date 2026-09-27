---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bank identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier that uniquely identifies the financial institution and, when appropriate, the branch of that financial
      institution servicing an account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bank number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankIdentifier
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: bank identifier
type: Ontology Class
---

# bank identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankIdentifier>

## Definition

identifier that uniquely identifies the financial institution and, when appropriate, the branch of that financial institution servicing an account

## Relationships

- **Subclass of**: [FinancialServiceProviderIdentifier](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label**: bank identifier
- **definition**: identifier that uniquely identifies the financial institution and, when appropriate, the branch of that financial institution servicing an account
- **adaptedFrom**: ISO 13616-1:2007 Financial services - International bank account number (IBAN)
- **synonym**: bank number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
