---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government-specified statistical area
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical area defined by a government agency
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalArea.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalArea
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: government-specified statistical area
type: Ontology Class
---

# government-specified statistical area

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea>

## Definition

statistical area defined by a government agency

## Relationships

- **Subclass of**: [StatisticalArea](/concepts/fibo/FND/Utilities/Analytics/StatisticalArea.md)

## Constraints

- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)

## Annotations

- **label**: government-specified statistical area
- **definition**: statistical area defined by a government agency

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
