---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: value-added producer price index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing a weighted average of the input and output producer price indices
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: value-added PPI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.imf.org/external/pubs/ft/ppi/2010/manual/ppi.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InputProducerPriceIndex
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/OutputProducerPriceIndex
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ValueAddedProducerPriceIndex
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: value-added producer price index
type: Ontology Class
---

# value-added producer price index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ValueAddedProducerPriceIndex>

## Definition

economic indicator representing a weighted average of the input and output producer price indices

## Relationships

- **Subclass of**: [ProducerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md)

## Constraints

- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: some values from of type [InputProducerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InputProducerPriceIndex.md)
- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: some values from of type [OutputProducerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/OutputProducerPriceIndex.md)

## Annotations

- **label**: value-added producer price index
- **definition**: economic indicator representing a weighted average of the input and output producer price indices
- **abbreviation**: value-added PPI
- **adaptedFrom**: https://www.imf.org/external/pubs/ft/ppi/2010/manual/ppi.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
