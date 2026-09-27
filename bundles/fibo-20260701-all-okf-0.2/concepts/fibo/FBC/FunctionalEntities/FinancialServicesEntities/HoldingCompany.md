---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: holding company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: business entity established to own stock in another company, typically to own enough voting shares to have some
      level of control over that company's policies and management
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Holding companies protect their owners from losses to some degree, protecting assets, for example, in case of bankruptcy.
      They can also be set up to own property such as real estate, patents, trademarks, stocks and other assets to limit financial
      and legal liability
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasPortfolioCompany
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/HoldingCompany
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: holding company
type: Ontology Class
---

# holding company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/HoldingCompany>

## Definition

business entity established to own stock in another company, typically to own enough voting shares to have some level of control over that company's policies and management

## Relationships

- **Subclass of**: [FunctionalBusinessEntity](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md)

## Constraints

- **[hasPortfolioCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/hasPortfolioCompany.md)**: min qualified cardinality 0 of type [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)

## Annotations

- **label**: holding company
- **definition**: business entity established to own stock in another company, typically to own enough voting shares to have some level of control over that company's policies and management
- **explanatoryNote**: Holding companies protect their owners from losses to some degree, protecting assets, for example, in case of bankruptcy. They can also be set up to own property such as real estate, patents, trademarks, stocks and other assets to limit financial and legal liability

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
