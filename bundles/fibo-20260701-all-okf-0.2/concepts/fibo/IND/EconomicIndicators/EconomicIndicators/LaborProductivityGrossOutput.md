---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: labor productivity, based on gross output
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ratio of a quantity index of gross output to a quantity index of labor input
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.oecd.org/std/productivity-stats/2352458.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Gross-output based labour productivity traces the labour requirements per unit of (physical) output. It reflects
      the change in the input coefficient of labour by industry and can help in the analysis of labour requirements by industry.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Shows the time profile of how productively labour is used to generate gross output. Labour productivity changes
      reflect the joint influence of changes in capital, intermediate inputs, as well as technical, organisational and efficiency
      change within and between firms, the influence of economies of scale, varying degrees of capacity utilisation and measurement
      errors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Productivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Productivity
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/LaborProductivityGrossOutput
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: labor productivity, based on gross output
type: Ontology Class
---

# labor productivity, based on gross output

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/LaborProductivityGrossOutput>

## Definition

ratio of a quantity index of gross output to a quantity index of labor input

## Relationships

- **Subclass of**: [Productivity](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Productivity.md)

## Annotations

- **label**: labor productivity, based on gross output
- **definition**: ratio of a quantity index of gross output to a quantity index of labor input
- **adaptedFrom**: http://www.oecd.org/std/productivity-stats/2352458.pdf
- **explanatoryNote**: Gross-output based labour productivity traces the labour requirements per unit of (physical) output. It reflects the change in the input coefficient of labour by industry and can help in the analysis of labour requirements by industry.
- **explanatoryNote**: Shows the time profile of how productively labour is used to generate gross output. Labour productivity changes reflect the joint influence of changes in capital, intermediate inputs, as well as technical, organisational and efficiency change within and between firms, the influence of economies of scale, varying degrees of capacity utilisation and measurement errors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
