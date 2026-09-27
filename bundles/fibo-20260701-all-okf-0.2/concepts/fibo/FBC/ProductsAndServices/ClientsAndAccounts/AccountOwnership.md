---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: account ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: holding of an account
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountAsAnAsset
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwnedAsset
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwningParty
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountOwnership
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: account ownership
type: Ontology Class
---

# account ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountOwnership>

## Definition

holding of an account

## Relationships

- **Subclass of**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)

## Constraints

- **[hasOwnedAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwnedAsset.md)**: exact qualified cardinality 1 of type [AccountAsAnAsset](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountAsAnAsset.md)
- **[hasOwningParty](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwningParty.md)**: some values from of type [AccountHolder](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)

## Annotations

- **label**: account ownership
- **definition**: holding of an account

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
