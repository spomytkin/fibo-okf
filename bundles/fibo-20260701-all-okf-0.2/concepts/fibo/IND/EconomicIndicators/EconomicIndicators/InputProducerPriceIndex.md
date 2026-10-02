---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: input producer price index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing measure of the rate of change over time in the prices of inputs of goods and services
      purchased by the producer
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: input PPI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.imf.org/external/pubs/ft/ppi/2010/manual/ppi.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InputProducerPriceIndex
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: input producer price index
type: Ontology Class
---

# input producer price index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InputProducerPriceIndex>

## Definition

economic indicator representing measure of the rate of change over time in the prices of inputs of goods and services purchased by the producer

## Relationships

- **Subclass of**: [ProducerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md)

## Annotations

- **label**: input producer price index
- **definition**: economic indicator representing measure of the rate of change over time in the prices of inputs of goods and services purchased by the producer
- **abbreviation**: input PPI
- **adaptedFrom**: https://www.imf.org/external/pubs/ft/ppi/2010/manual/ppi.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
