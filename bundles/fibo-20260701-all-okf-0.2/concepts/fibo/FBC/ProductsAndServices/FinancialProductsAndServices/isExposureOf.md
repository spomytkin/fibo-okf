---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is exposure of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: is the influence or risk borne by
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isExposureOf
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: is exposure of
type: Ontology Property
---

# is exposure of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isExposureOf>

## Definition

is the influence or risk borne by

## Relationships

- **Domain**: [Exposure](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md)
- **Range**: [ExposureBearer](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer.md)
- **Subproperty of**: [isAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy>)

## Annotations

- **label**: is exposure of
- **definition**: is the influence or risk borne by

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
