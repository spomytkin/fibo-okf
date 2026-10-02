---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: labor productivity, based on value added
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ratio of a quantity index of value added to a quantity index of labor input
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.oecd.org/std/productivity-stats/2352458.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: At the aggregate level, value-added based labour productivity forms a direct link to a widely used measure of living
      standards, income per capita. Productivity translates directly into living standards, by adjusting for changing working
      hours, unemployment, labour force participation rates and demographic changes.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Shows the time profile of how productively labour is used to generate value added. Labour productivity changes
      reflect the joint influence of changes in capital, as well as technical, organisational and efficiency change within
      and between firms, the influence of economies of scale, varying degrees of capacity utilisation and measurement errors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Productivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Productivity
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/LaborProductivityValueAdded
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: labor productivity, based on value added
type: Ontology Class
---

# labor productivity, based on value added

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/LaborProductivityValueAdded>

## Definition

ratio of a quantity index of value added to a quantity index of labor input

## Relationships

- **Subclass of**: [Productivity](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Productivity.md)

## Annotations

- **label**: labor productivity, based on value added
- **definition**: ratio of a quantity index of value added to a quantity index of labor input
- **adaptedFrom**: http://www.oecd.org/std/productivity-stats/2352458.pdf
- **explanatoryNote**: At the aggregate level, value-added based labour productivity forms a direct link to a widely used measure of living standards, income per capita. Productivity translates directly into living standards, by adjusting for changing working hours, unemployment, labour force participation rates and demographic changes.
- **explanatoryNote**: Shows the time profile of how productively labour is used to generate value added. Labour productivity changes reflect the joint influence of changes in capital, as well as technical, organisational and efficiency change within and between firms, the influence of economies of scale, varying degrees of capacity utilisation and measurement errors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
