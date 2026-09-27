---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: energy resource
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: negotiable commodity that is an energy-related product, or a derivative of an energy-related product, including
      electricity, renewable energy, or any power/energy delivered through a utility network of provider; diesel fuel, fuel
      oil, gas oil, gasoline, heating oil, jet fuel, kerosene, natural gas, oil (Brent, Tapis, Dubai, WTI)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: Note that the concept of an energy resource overlaps with generated resource and extraction resource but is not
      identical to either.
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
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/EnergyResource
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: energy resource
type: Ontology Class
---

# energy resource

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/EnergyResource>

## Definition

negotiable commodity that is an energy-related product, or a derivative of an energy-related product, including electricity, renewable energy, or any power/energy delivered through a utility network of provider; diesel fuel, fuel oil, gas oil, gasoline, heating oil, jet fuel, kerosene, natural gas, oil (Brent, Tapis, Dubai, WTI)

## Relationships

- **Subclass of**: [NegotiableCommodity](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/NegotiableCommodity.md)

## Annotations

- **label** (en): energy resource
- **definition** (en): negotiable commodity that is an energy-related product, or a derivative of an energy-related product, including electricity, renewable energy, or any power/energy delivered through a utility network of provider; diesel fuel, fuel oil, gas oil, gasoline, heating oil, jet fuel, kerosene, natural gas, oil (Brent, Tapis, Dubai, WTI)
- **scopeNote** (en): Note that the concept of an energy resource overlaps with generated resource and extraction resource but is not identical to either.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
