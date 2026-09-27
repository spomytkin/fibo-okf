---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: community investment fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'professionally-managed investment fund with three essential characteristics: capital is sourced from people in
      the community (ideally from retail/non-accredited investors); capital is invested into local people, projects, and businesses;
      and capital is deployed by individuals in the community, typically but not necessarily a nonprofit fund'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CIF
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Community Investment Fund Handbook and Toolkit, available at https://www.nc3now.org/community-investment-fund-handbook--toolkit.html.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A community investment fund is typically but not necessarily a nonprofit fund.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/LocalInvestmentObjective
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - filler: https://www.omg.org/spec/Commons/Locations/GeographicRegion
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Locations/hasCoverageArea
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/PrivateFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PrivateFund
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/CommunityInvestmentFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: community investment fund
type: Ontology Class
---

# community investment fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/CommunityInvestmentFund>

## Definition

professionally-managed investment fund with three essential characteristics: capital is sourced from people in the community (ideally from retail/non-accredited investors); capital is invested into local people, projects, and businesses; and capital is deployed by individuals in the community, typically but not necessarily a nonprofit fund

## Relationships

- **Subclass of**: [PrivateFund](/concepts/fibo/SEC/Securities/Pools/PrivateFund.md)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: some values from of type [LocalInvestmentObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/LocalInvestmentObjective.md)
- **[hasCoverageArea](<https://www.omg.org/spec/Commons/Locations/hasCoverageArea>)**: some values from of type [GeographicRegion](<https://www.omg.org/spec/Commons/Locations/GeographicRegion>)

## Annotations

- **label** (en): community investment fund
- **definition** (en): professionally-managed investment fund with three essential characteristics: capital is sourced from people in the community (ideally from retail/non-accredited investors); capital is invested into local people, projects, and businesses; and capital is deployed by individuals in the community, typically but not necessarily a nonprofit fund
- **abbreviation** (en): CIF
- **adaptedFrom** (en): Community Investment Fund Handbook and Toolkit, available at https://www.nc3now.org/community-investment-fund-handbook--toolkit.html.
- **explanatoryNote** (en): A community investment fund is typically but not necessarily a nonprofit fund.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
