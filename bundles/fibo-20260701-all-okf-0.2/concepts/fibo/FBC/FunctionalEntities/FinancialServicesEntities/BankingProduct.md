---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: banking product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: product provided to consumers and businesses by a depository institution
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include checking account, savings account, certificate of deposit, debit or pre-paid card, or credit card.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BankingProduct
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: banking product
type: Ontology Class
---

# banking product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BankingProduct>

## Definition

product provided to consumers and businesses by a depository institution

## Relationships

- **Subclass of**: [FinancialProduct](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)

## Constraints

- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [DepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)

## Annotations

- **label**: banking product
- **definition**: product provided to consumers and businesses by a depository institution
- **example**: Examples include checking account, savings account, certificate of deposit, debit or pre-paid card, or credit card.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
