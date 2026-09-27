---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: nonprofit fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment vehicle designed to support a nonprofit mission, whose objectives include environmental stewardship
      and/or social responsibility in addition to financial performance
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Common examples include endowment funds (permanently invested, only earnings are spent), operating funds (used
      for day-to-day expenses), and special project funds (earmarked for particular initiatives).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A nonprofit fund is a pool of financial resources that is established and managed by a nonprofit organization to
      support its mission and activities, organized for charitable, educational, religious, cultural, or other purposes recognized
      as serving the public good. Some nonprofit funds are restricted by donors for a specific use (such as an endowment for
      scholarships), while others are unrestricted and can be used at the nonprofit's discretion.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/TripleBottomLineObjective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/PrivateFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PrivateFund
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/NonprofitFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: nonprofit fund
type: Ontology Class
---

# nonprofit fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/NonprofitFund>

## Definition

investment vehicle designed to support a nonprofit mission, whose objectives include environmental stewardship and/or social responsibility in addition to financial performance

## Relationships

- **Subclass of**: [PrivateFund](/concepts/fibo/SEC/Securities/Pools/PrivateFund.md)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [TripleBottomLineObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/TripleBottomLineObjective.md)

## Annotations

- **label** (en): nonprofit fund
- **definition** (en): investment vehicle designed to support a nonprofit mission, whose objectives include environmental stewardship and/or social responsibility in addition to financial performance
- **example** (en): Common examples include endowment funds (permanently invested, only earnings are spent), operating funds (used for day-to-day expenses), and special project funds (earmarked for particular initiatives).
- **explanatoryNote** (en): A nonprofit fund is a pool of financial resources that is established and managed by a nonprofit organization to support its mission and activities, organized for charitable, educational, religious, cultural, or other purposes recognized as serving the public good. Some nonprofit funds are restricted by donors for a specific use (such as an endowment for scholarships), while others are unrestricted and can be used at the nonprofit's discretion.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
