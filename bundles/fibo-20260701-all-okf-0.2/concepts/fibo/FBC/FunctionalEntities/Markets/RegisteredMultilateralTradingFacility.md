---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registered multilateral trading facility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: multilateral system operated by an investment firm or market operator, which brings together multiple third-party
      buying and selling interests in financial instruments in the system, in accordance with non-discretionary rules, in
      a way that results in a contract in accordance with the provisions of Title II of the MiFID II
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  - filler: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/MultilateralTradingFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegisteredMultilateralTradingFacility
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: registered multilateral trading facility
type: Ontology Class
---

# registered multilateral trading facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegisteredMultilateralTradingFacility>

## Definition

multilateral system operated by an investment firm or market operator, which brings together multiple third-party buying and selling interests in financial instruments in the system, in accordance with non-discretionary rules, in a way that results in a contract in accordance with the provisions of Title II of the MiFID II

## Relationships

- **Subclass of**: [MultilateralTradingFacility](/concepts/fibo/FBC/FunctionalEntities/Markets/MultilateralTradingFacility.md)

## Constraints

- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from of type [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: some values from of type [RegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority>)
- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: registered multilateral trading facility
- **definition**: multilateral system operated by an investment firm or market operator, which brings together multiple third-party buying and selling interests in financial instruments in the system, in accordance with non-discretionary rules, in a way that results in a contract in accordance with the provisions of Title II of the MiFID II

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
