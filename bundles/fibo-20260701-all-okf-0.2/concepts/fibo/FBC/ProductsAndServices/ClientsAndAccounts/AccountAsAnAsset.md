---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: account as an asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial asset in the form of an account
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isAssetOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountAsAnAsset
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: account as an asset
type: Ontology Class
---

# account as an asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountAsAnAsset>

## Definition

financial asset in the form of an account

## Relationships

- **Subclass of**: [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)

## Constraints

- **[isAssetOf](/concepts/fibo/FND/OwnershipAndControl/Ownership/isAssetOf.md)**: some values from of type [AccountHolder](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Annotations

- **label**: account as an asset
- **definition**: financial asset in the form of an account

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
