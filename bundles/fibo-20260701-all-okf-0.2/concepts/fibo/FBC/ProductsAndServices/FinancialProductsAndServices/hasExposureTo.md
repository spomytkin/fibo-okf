---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has exposure to
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: involves influence or risk from
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation
  inverse_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/exposesIn.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/exposesIn
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasExposureTo
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: has exposure to
type: Ontology Property
---

# has exposure to

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasExposureTo>

## Definition

involves influence or risk from

## Relationships

- **Domain**: [ExposureSituation](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation.md)
- **Inverse of**: [exposesIn](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/exposesIn.md)
- **Range**: [Exposure](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md)
- **Subproperty of**: [hasUndergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer>)

## Annotations

- **label**: has exposure to
- **definition**: involves influence or risk from

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
