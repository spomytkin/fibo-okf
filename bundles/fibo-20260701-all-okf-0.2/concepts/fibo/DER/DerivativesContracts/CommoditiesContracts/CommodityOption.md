---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option where the option buyer has the right to buy or sell specified commodities or commodity related index at
      a fixed price or formula, on or before a specified date
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019-10
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityOption
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: commodity option
type: Ontology Class
---

# commodity option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityOption>

## Definition

option where the option buyer has the right to buy or sell specified commodities or commodity related index at a fixed price or formula, on or before a specified date

## Relationships

- **Subclass of**: [CommodityDerivative](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- **Subclass of**: [VanillaOption](/concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md)

## Annotations

- **label** (en): commodity option
- **definition** (en): option where the option buyer has the right to buy or sell specified commodities or commodity related index at a fixed price or formula, on or before a specified date
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
