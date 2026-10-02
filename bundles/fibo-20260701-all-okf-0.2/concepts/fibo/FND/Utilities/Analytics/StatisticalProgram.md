---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statistical program
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: program that presents a detailed investigation and analysis of a subject or situation involving one or more studies
      or surveys
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalUniverse
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalArea
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Locations/hasCoverageArea
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Program.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Program
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalProgram
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: statistical program
type: Ontology Class
---

# statistical program

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalProgram>

## Definition

program that presents a detailed investigation and analysis of a subject or situation involving one or more studies or surveys

## Relationships

- **Subclass of**: [Program](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Program.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [StatisticalUniverse](/concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md)
- **[hasCoverageArea](<https://www.omg.org/spec/Commons/Locations/hasCoverageArea>)**: some values from of type [StatisticalArea](/concepts/fibo/FND/Utilities/Analytics/StatisticalArea.md)
- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [StatisticalMeasure](/concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md)

## Annotations

- **label**: statistical program
- **definition**: program that presents a detailed investigation and analysis of a subject or situation involving one or more studies or surveys

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
