---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is subject to reserve requirements
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether some capability of a financial service provider is contingent on conformance with certain Federal
      Reserve policies, regulations, or other requirements
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/isSubjectToReserveRequirements
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: is subject to reserve requirements
type: Ontology Property
---

# is subject to reserve requirements

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/isSubjectToReserveRequirements>

## Definition

indicates whether some capability of a financial service provider is contingent on conformance with certain Federal Reserve policies, regulations, or other requirements

## Relationships

- **Domain**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is subject to reserve requirements
- **definition**: indicates whether some capability of a financial service provider is contingent on conformance with certain Federal Reserve policies, regulations, or other requirements

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
