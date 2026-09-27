---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capital-labor multifactor productivity (MFP), based on value added
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ratio of a quantity index of value added to a quantity index of combined labor and capital input
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.oecd.org/std/productivity-stats/2352458.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Capital-labour MFP indices show the time profile of how productively combined labour and capital inputs are used
      to generate value added. Conceptually, capital-labour productivity is not, in general, an accurate measure of technical
      change. It is, however, an indicator of an industry's capacity to contribute to economy-wide growth of income per unit
      of primary input. In practice, the measure reflects the combined effects of disembodied technical change, economies
      of scale, efficiency change, variations in capacity utilisation and measurement errors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Productivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Productivity
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CapitalLaborMultifactorProductivityValueAdded
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: capital-labor multifactor productivity (MFP), based on value added
type: Ontology Class
---

# capital-labor multifactor productivity (MFP), based on value added

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CapitalLaborMultifactorProductivityValueAdded>

## Definition

ratio of a quantity index of value added to a quantity index of combined labor and capital input

## Relationships

- **Subclass of**: [Productivity](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Productivity.md)

## Annotations

- **label**: capital-labor multifactor productivity (MFP), based on value added
- **definition**: ratio of a quantity index of value added to a quantity index of combined labor and capital input
- **adaptedFrom**: http://www.oecd.org/std/productivity-stats/2352458.pdf
- **explanatoryNote**: Capital-labour MFP indices show the time profile of how productively combined labour and capital inputs are used to generate value added. Conceptually, capital-labour productivity is not, in general, an accurate measure of technical change. It is, however, an indicator of an industry's capacity to contribute to economy-wide growth of income per unit of primary input. In practice, the measure reflects the combined effects of disembodied technical change, economies of scale, efficiency change, variations in capacity utilisation and measurement errors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
