---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: enterprise population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical universe consisting of enterprises designed for the purposes of supporting surveys such as those used
      as the basis for employment and producer price indices
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Enterprise
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalUniverse
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EnterprisePopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: enterprise population
type: Ontology Class
---

# enterprise population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EnterprisePopulation>

## Definition

statistical universe consisting of enterprises designed for the purposes of supporting surveys such as those used as the basis for employment and producer price indices

## Relationships

- **Subclass of**: [StatisticalUniverse](/concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [Enterprise](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Enterprise.md)

## Annotations

- **label**: enterprise population
- **definition**: statistical universe consisting of enterprises designed for the purposes of supporting surveys such as those used as the basis for employment and producer price indices

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
