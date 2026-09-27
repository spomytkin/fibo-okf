---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial service provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: functional entity either licensed to provide financial services to consumers and/or businesses or established by
      law to provide financial services, such as a central bank
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Organizations/LegalEntity
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: financial service provider
type: Ontology Class
---

# financial service provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider>

## Definition

functional entity either licensed to provide financial services to consumers and/or businesses or established by law to provide financial services, such as a central bank

## Relationships

- **Subclass of**: [FunctionalBusinessEntity](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md)
- **Subclass of**: [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)

## Constraints

- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [FinancialService](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label**: financial service provider
- **definition**: functional entity either licensed to provide financial services to consumers and/or businesses or established by law to provide financial services, such as a central bank

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
