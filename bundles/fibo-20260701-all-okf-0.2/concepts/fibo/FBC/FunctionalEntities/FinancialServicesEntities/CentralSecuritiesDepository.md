---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: central securities depository
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: functional entity that provides a central point for depositing financial instruments ('securities'), for example,
      bonds and shares
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CSD
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://ecsda.eu/facts/faq
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: CSDs' clients are typically financial institutions themselves (such as custodian banks and brokers) rather than
      individual investors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralSecuritiesDepository
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: central securities depository
type: Ontology Class
---

# central securities depository

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralSecuritiesDepository>

## Definition

functional entity that provides a central point for depositing financial instruments ('securities'), for example, bonds and shares

## Relationships

- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Annotations

- **label**: central securities depository
- **definition**: functional entity that provides a central point for depositing financial instruments ('securities'), for example, bonds and shares
- **abbreviation**: CSD
- **adaptedFrom**: http://ecsda.eu/facts/faq
- **explanatoryNote**: CSDs' clients are typically financial institutions themselves (such as custodian banks and brokers) rather than individual investors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
