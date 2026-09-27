---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has indicator value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a quantity value for a given indicator
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasIndicatorValue
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: has indicator value
type: Ontology Property
---

# has indicator value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasIndicatorValue>

## Definition

specifies a quantity value for a given indicator

## Relationships

- **Range**: [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)
- **Subproperty of**: [hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)

## Annotations

- **label**: has indicator value
- **definition**: specifies a quantity value for a given indicator

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
