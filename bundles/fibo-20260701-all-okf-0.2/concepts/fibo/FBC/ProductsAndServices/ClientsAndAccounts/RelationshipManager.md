---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: relationship manager
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: responsible party who manages a client's account and oversees their relationship with the service provider
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: account manager
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/manages
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/RelationshipManager
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: relationship manager
type: Ontology Class
---

# relationship manager

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/RelationshipManager>

## Definition

responsible party who manages a client's account and oversees their relationship with the service provider

## Relationships

- **Subclass of**: [ResponsibleParty](<https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty>)

## Constraints

- **[manages](<https://www.omg.org/spec/Commons/Organizations/manages>)**: some values from of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Annotations

- **label**: relationship manager
- **definition**: responsible party who manages a client's account and oversees their relationship with the service provider
- **synonym**: account manager

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
