---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registered investment advisor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registered agent and financial service provider that advises high net worth individuals on investments and manages
      their portfolios
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: RIA
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/advises
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: N81bafdb53ee94146b644dbd429affd95
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/RegisteredInvestmentAdvisor
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: registered investment advisor
type: Ontology Class
---

# registered investment advisor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/RegisteredInvestmentAdvisor>

## Definition

registered agent and financial service provider that advises high net worth individuals on investments and manages their portfolios

## Relationships

- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- **Subclass of**: [RegisteredAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md)

## Constraints

- **[advises](/concepts/fibo/BE/OwnershipAndControl/ControlParties/advises.md)**: some values from of type [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: some values from value `N81bafdb53ee94146b644dbd429affd95`

## Annotations

- **label**: registered investment advisor
- **definition**: registered agent and financial service provider that advises high net worth individuals on investments and manages their portfolios
- **abbreviation**: RIA

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
