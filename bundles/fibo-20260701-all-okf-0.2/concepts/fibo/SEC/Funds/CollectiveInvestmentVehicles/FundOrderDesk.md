---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund order desk
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The Fund Order Desk is a party to the Fund Order Desk Account.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: This party would presumably be identified as the Fund Management Company in terms of what legal entity fulcils
      this role? to be determined at further review.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalEntity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundOrderDesk
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund order desk
type: Ontology Class
---

# fund order desk

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundOrderDesk>

## Definition

The Fund Order Desk is a party to the Fund Order Desk Account.

## Relationships

- **Subclass of**: [AccountProvider](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label** (en): fund order desk
- **definition** (en): The Fund Order Desk is a party to the Fund Order Desk Account.
- **editorialNote** (en): This party would presumably be identified as the Fund Management Company in terms of what legal entity fulcils this role? to be determined at further review.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
