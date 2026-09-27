---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agricultural resource
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: negotiable commodity that is obtained via some agricultural process, including forestry, fishing, livestock, grain,
      dairy, corn, cocoa, soybeans, sugar, coffee
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019-10
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/NegotiableCommodity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/NegotiableCommodity
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/AgriculturalResource
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: agricultural resource
type: Ontology Class
---

# agricultural resource

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/AgriculturalResource>

## Definition

negotiable commodity that is obtained via some agricultural process, including forestry, fishing, livestock, grain, dairy, corn, cocoa, soybeans, sugar, coffee

## Relationships

- **Subclass of**: [NegotiableCommodity](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/NegotiableCommodity.md)

## Annotations

- **label** (en): agricultural resource
- **definition** (en): negotiable commodity that is obtained via some agricultural process, including forestry, fishing, livestock, grain, dairy, corn, cocoa, soybeans, sugar, coffee
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
