---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed basket population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical universe consisting of specific goods and/or services designed for the purposes of supporting surveys
      such as those used as the basis for price indices
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.imf.org/external/pubs/ft/ppi/2010/manual/ppi.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: goods and services population
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: goods and/or services population
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: N9e08a505c7c846e79133b1007084f5df
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalUniverse
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/FixedBasketPopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: fixed basket population
type: Ontology Class
---

# fixed basket population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/FixedBasketPopulation>

## Definition

statistical universe consisting of specific goods and/or services designed for the purposes of supporting surveys such as those used as the basis for price indices

## Relationships

- **Subclass of**: [StatisticalUniverse](/concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `N9e08a505c7c846e79133b1007084f5df`

## Annotations

- **label**: fixed basket population
- **definition**: statistical universe consisting of specific goods and/or services designed for the purposes of supporting surveys such as those used as the basis for price indices
- **adaptedFrom**: https://www.imf.org/external/pubs/ft/ppi/2010/manual/ppi.pdf
- **synonym**: goods and services population
- **synonym**: goods and/or services population

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
