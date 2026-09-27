---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment objective
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial objective used by an investor to determine whether or not a given potential investment is appropriate
      for themselves or on behalf of another party
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: An investor whose objective is capital growth might choose to invest in more aggressive, growth-oriented mutual
      funds and/or stocks, over income-generating mutual funds and/or bonds.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The combination of investment objectives and risk tolerance are typically used to identify appropriate investment
      options.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/FinancialObjective.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/FinancialObjective
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/InvestmentObjective
sources:
- id: fibo-source-f0b2e96255
  resource: references/fibo/FND/GoalsAndObjectives/Objectives.rdf
  sha256: f0b2e962552cee4f3cce3b136e48393e8ca4cae011a4c4cb80f887f6030a97a4
  title: FIBO source FND/GoalsAndObjectives/Objectives.rdf
title: investment objective
type: Ontology Class
---

# investment objective

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/InvestmentObjective>

## Definition

financial objective used by an investor to determine whether or not a given potential investment is appropriate for themselves or on behalf of another party

## Relationships

- **Subclass of**: [FinancialObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/FinancialObjective.md)

## Annotations

- **label**: investment objective
- **definition**: financial objective used by an investor to determine whether or not a given potential investment is appropriate for themselves or on behalf of another party
- **example**: An investor whose objective is capital growth might choose to invest in more aggressive, growth-oriented mutual funds and/or stocks, over income-generating mutual funds and/or bonds.
- **explanatoryNote**: The combination of investment objectives and risk tolerance are typically used to identify appropriate investment options.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
