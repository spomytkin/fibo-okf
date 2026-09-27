---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: funds processing account
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An account used specifically in the processing of funds. Like all accounts this is (per FIBIM definition) a business
      relationship between two entities; one entity is the account owner, the other entity is the account servicer. Please
      refer to Financial global model for treatment of accounts relationships in this model.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Derived from FIBIM definition for "Account", which is: "Business relationship between two entities; one entity
      is the account owner, the other entity is the account servicer." this corresponds to the Global Terms definition for
      Account.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundOrderDesk
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingAccount
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: funds processing account
type: Ontology Class
---

# funds processing account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingAccount>

## Definition

An account used specifically in the processing of funds. Like all accounts this is (per FIBIM definition) a business relationship between two entities; one entity is the account owner, the other entity is the account servicer. Please refer to Financial global model for treatment of accounts relationships in this model.

## Relationships

- **Subclass of**: [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Constraints

- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [FundOrderDesk](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundOrderDesk.md)

## Annotations

- **label** (en): funds processing account
- **definition** (en): An account used specifically in the processing of funds. Like all accounts this is (per FIBIM definition) a business relationship between two entities; one entity is the account owner, the other entity is the account servicer. Please refer to Financial global model for treatment of accounts relationships in this model.
- **explanatoryNote** (en): Derived from FIBIM definition for "Account", which is: "Business relationship between two entities; one entity is the account owner, the other entity is the account servicer." this corresponds to the Global Terms definition for Account.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
