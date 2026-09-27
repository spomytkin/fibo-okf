---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: merchant service
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service provided by a financial institution to a merchant or other business, including but not limited
      to managing financial transactions via a secure channel
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Example merchant services include credit and debit card processing, check guarantee and conversion services, point
      of sale (PoS) systems, gift card and loyalty programs, online transaction processing, etc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MerchantService
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: merchant service
type: Ontology Class
---

# merchant service

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MerchantService>

## Definition

financial service provided by a financial institution to a merchant or other business, including but not limited to managing financial transactions via a secure channel

## Relationships

- **Subclass of**: [FinancialService](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)

## Annotations

- **label**: merchant service
- **definition**: financial service provided by a financial institution to a merchant or other business, including but not limited to managing financial transactions via a secure channel
- **example**: Example merchant services include credit and debit card processing, check guarantee and conversion services, point of sale (PoS) systems, gift card and loyalty programs, online transaction processing, etc.
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
