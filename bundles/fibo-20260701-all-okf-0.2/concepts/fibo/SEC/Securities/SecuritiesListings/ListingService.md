---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: listing service
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: service provided by an exchange to facilitate securities trading
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/isProvisionedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/provides
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListingService
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: listing service
type: Ontology Class
---

# listing service

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListingService>

## Definition

service provided by an exchange to facilitate securities trading

## Relationships

- **Subclass of**: [FinancialService](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)

## Constraints

- **[isProvisionedBy](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/isProvisionedBy.md)**: min qualified cardinality 0 of type [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: min qualified cardinality 0 of type [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)
- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: min qualified cardinality 0 of type [Listing](/concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md)

## Annotations

- **label**: listing service
- **definition**: service provided by an exchange to facilitate securities trading

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
