---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: account-specific service agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: service-agreement that is account-specific, applicable in cases where a client might hold multiple accounts with
      differing terms and conditions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Customers of financial service providers frequently hold multiple accounts - brokerage accounts, checking and savings
      accounts, trust accounts, and so forth - which may have specific terms and conditions associated with them.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountSpecificServiceAgreement
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: account-specific service agreement
type: Ontology Class
---

# account-specific service agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountSpecificServiceAgreement>

## Definition

service-agreement that is account-specific, applicable in cases where a client might hold multiple accounts with differing terms and conditions

## Relationships

- **Subclass of**: [ServiceAgreement](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement.md)

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [AccountHolder](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)
- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [AccountProvider](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Annotations

- **label**: account-specific service agreement
- **definition**: service-agreement that is account-specific, applicable in cases where a client might hold multiple accounts with differing terms and conditions
- **explanatoryNote**: Customers of financial service providers frequently hold multiple accounts - brokerage accounts, checking and savings accounts, trust accounts, and so forth - which may have specific terms and conditions associated with them.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
