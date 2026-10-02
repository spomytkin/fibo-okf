---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payroll service
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service, typically provided to small businesses that are not large enough to have an internal finance
      organization, that involves managing payment of wages to employees
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Payroll services typically include printing of employee pay checks, direct deposit of wages to employee bank accounts,
      calculation and withholding of employee taxes, calculation and payment of corporate payroll taxes and fees with appropriate
      government authorities (such as Social Security in the US), filing government quarterly and annual reports, and so forth.
      They may also include management of retirement and savings plans, health benefits, timekeeping, automated integration
      with the business' accounting system, etc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/PayrollService
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: payroll service
type: Ontology Class
---

# payroll service

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/PayrollService>

## Definition

financial service, typically provided to small businesses that are not large enough to have an internal finance organization, that involves managing payment of wages to employees

## Relationships

- **Subclass of**: [FinancialService](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)

## Annotations

- **label**: payroll service
- **definition**: financial service, typically provided to small businesses that are not large enough to have an internal finance organization, that involves managing payment of wages to employees
- **explanatoryNote**: Payroll services typically include printing of employee pay checks, direct deposit of wages to employee bank accounts, calculation and withholding of employee taxes, calculation and payment of corporate payroll taxes and fees with appropriate government authorities (such as Social Security in the US), filing government quarterly and annual reports, and so forth. They may also include management of retirement and savings plans, health benefits, timekeeping, automated integration with the business' accounting system, etc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
