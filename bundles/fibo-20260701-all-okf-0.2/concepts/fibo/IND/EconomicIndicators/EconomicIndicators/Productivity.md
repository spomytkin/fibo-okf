---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: productivity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing ratio of a volume measure of output to a volume measure of input use
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=2167
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.oecd.org/std/productivity-stats/2352458.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The primary objectives of productivity measurement include: (a) tracing technology change, i.e., the currently
      known ways of converting resources into outputs desired by the economy, (b) identifying changes in efficiency, (c) understanding
      real cost savings, (d) benchmarking production processes, and (e) assessing standards of living. Productivity measures
      may also be single factor or multifactor.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Productivity
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: productivity
type: Ontology Class
---

# productivity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Productivity>

## Definition

economic indicator representing ratio of a volume measure of output to a volume measure of input use

## Relationships

- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Annotations

- **label**: productivity
- **definition**: economic indicator representing ratio of a volume measure of output to a volume measure of input use
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=2167
- **adaptedFrom**: http://www.oecd.org/std/productivity-stats/2352458.pdf
- **explanatoryNote**: The primary objectives of productivity measurement include: (a) tracing technology change, i.e., the currently known ways of converting resources into outputs desired by the economy, (b) identifying changes in efficiency, (c) understanding real cost savings, (d) benchmarking production processes, and (e) assessing standards of living. Productivity measures may also be single factor or multifactor.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
