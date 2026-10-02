---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has secondary account holder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an account to a client or customer that is considered a secondary, co-owner of the account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has account co-owner
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has secondary account owner
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/isHeldBy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasSecondaryAccountHolder
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: has secondary account holder
type: Ontology Property
---

# has secondary account holder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasSecondaryAccountHolder>

## Definition

relates an account to a client or customer that is considered a secondary, co-owner of the account

## Relationships

- **Domain**: [CustomerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
- **Range**: [CustomerAccountHolder](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder.md)
- **Subproperty of**: [isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)

## Annotations

- **label**: has secondary account holder
- **definition**: relates an account to a client or customer that is considered a secondary, co-owner of the account
- **synonym**: has account co-owner
- **synonym**: has secondary account owner

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
