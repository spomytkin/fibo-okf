---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: clearing house
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service provider that is exchange affiliated and provides clearing services, including the validation,
      delivery, and settlement of financial transactions, for financial intermediaries
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingService
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: clearing house
type: Ontology Class
---

# clearing house

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse>

## Definition

financial service provider that is exchange affiliated and provides clearing services, including the validation, delivery, and settlement of financial transactions, for financial intermediaries

## Relationships

- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Constraints

- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [ClearingService](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ClearingService.md)

## Annotations

- **label**: clearing house
- **definition**: financial service provider that is exchange affiliated and provides clearing services, including the validation, delivery, and settlement of financial transactions, for financial intermediaries
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
