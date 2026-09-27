---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: account holder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that owns an account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An account holder is named on the account and is authorized to conduct transactions associated with the account.
      Authorization is typically evidenced by signatures maintained on file by the account provider.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that this concept of account holder applies to internal accounts that are non-general ledger accounts also
      have account holders, such as payroll accounts, internal checking accounts associated with cashier's checks, and so
      forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N2bf4433a571a40169f4deba0b867dc26
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N5f6d68ec926b4ae2b465625ad9216a9f
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: account holder
type: Ontology Class
---

# account holder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder>

## Definition

party that owns an account

## Relationships

- **Subclass of**: [Owner](/concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md)

## Constraints

- **[holds](/concepts/fibo/FND/Relations/Relations/holds.md)**: some values from of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N2bf4433a571a40169f4deba0b867dc26`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N5f6d68ec926b4ae2b465625ad9216a9f`

## Annotations

- **label**: account holder
- **definition**: party that owns an account
- **explanatoryNote**: An account holder is named on the account and is authorized to conduct transactions associated with the account. Authorization is typically evidenced by signatures maintained on file by the account provider.
- **explanatoryNote**: Note that this concept of account holder applies to internal accounts that are non-general ledger accounts also have account holders, such as payroll accounts, internal checking accounts associated with cashier's checks, and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
