---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: excludes energy and food
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the calculation of the index includes energy and food prices or not
  domain:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/excludesEnergyAndFood
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: excludes energy and food
type: Ontology Property
---

# excludes energy and food

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/excludesEnergyAndFood>

## Definition

indicates whether the calculation of the index includes energy and food prices or not

## Relationships

- **Domain**: [ConsumerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: excludes energy and food
- **definition**: indicates whether the calculation of the index includes energy and food prices or not

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
