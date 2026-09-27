---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: international bank of US depositary, edge, trust company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bank that is owned or controlled by a US depository institution, Edge Act corporation or trust company
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-IBK
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
    value: N342e7a19cd0d4a9c9d11b0ada151f1fa
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/InternationalBankOfUSDepositoryEdgeTrustCompany
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: international bank of US depositary, edge, trust company
type: Ontology Class
---

# international bank of US depositary, edge, trust company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/InternationalBankOfUSDepositoryEdgeTrustCompany>

## Definition

bank that is owned or controlled by a US depository institution, Edge Act corporation or trust company

## Relationships

- **Subclass of**: [Bank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-IBK`
- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from value `N342e7a19cd0d4a9c9d11b0ada151f1fa`

## Annotations

- **label**: international bank of US depositary, edge, trust company
- **definition**: bank that is owned or controlled by a US depository institution, Edge Act corporation or trust company

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
