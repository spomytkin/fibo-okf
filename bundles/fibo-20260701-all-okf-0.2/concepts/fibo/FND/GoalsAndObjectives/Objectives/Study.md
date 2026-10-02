---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: study
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: analytical activity that investigates a specified area of interest, to determine its characteristics, relationships,
      constraints, or implications
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Studies involve exploration, analysis, sometimes modeling, and sometimes evaluation, but are not necessarily focused
      on evaluation and may or may not be criteria-based, which distinguishes it from the concept of an assessment. In a business
      context, a study might map capabilities, analyze value streams, or model information flows. Only some studies produce
      an assessment (e.g., capability maturity assessment). A clinical research study may observe, test, or model phenomena,
      and may or may not result in a clinical or risk assessment. A study conducted as part of a project or larger programme
      may explore feasibility, options, impacts, or requirements.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Goal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasGoal
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/ContextualDesignators/Context
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Study
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: study
type: Ontology Class
---

# study

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Study>

## Definition

analytical activity that investigates a specified area of interest, to determine its characteristics, relationships, constraints, or implications

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[hasGoal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasGoal.md)**: min qualified cardinality 0 of type [Goal](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Goal.md)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: min qualified cardinality 0 of type [Context](<https://www.omg.org/spec/Commons/ContextualDesignators/Context>)

## Annotations

- **label**: study
- **definition**: analytical activity that investigates a specified area of interest, to determine its characteristics, relationships, constraints, or implications
- **explanatoryNote** (en): Studies involve exploration, analysis, sometimes modeling, and sometimes evaluation, but are not necessarily focused on evaluation and may or may not be criteria-based, which distinguishes it from the concept of an assessment. In a business context, a study might map capabilities, analyze value streams, or model information flows. Only some studies produce an assessment (e.g., capability maturity assessment). A clinical research study may observe, test, or model phenomena, and may or may not result in a clinical or risk assessment. A study conducted as part of a project or larger programme may explore feasibility, options, impacts, or requirements.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
