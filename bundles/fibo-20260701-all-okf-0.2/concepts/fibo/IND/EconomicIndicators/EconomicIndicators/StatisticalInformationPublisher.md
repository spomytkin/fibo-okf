---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statistical information publisher
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: publisher that packages and makes analytical and statistical data available
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/StatisticalInformationPublisher
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: statistical information publisher
type: Ontology Class
---

# statistical information publisher

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/StatisticalInformationPublisher>

## Definition

publisher that packages and makes analytical and statistical data available

## Relationships

- **Subclass of**: [Publisher](/concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)

## Annotations

- **label**: statistical information publisher
- **definition**: publisher that packages and makes analytical and statistical data available

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
