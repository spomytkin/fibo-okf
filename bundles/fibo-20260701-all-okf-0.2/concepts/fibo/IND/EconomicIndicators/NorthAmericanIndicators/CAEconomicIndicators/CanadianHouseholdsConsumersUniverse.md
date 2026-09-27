---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Canadian households consumers universe
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a statistical universe consisting of all private households in Canada, with the exception of soldiers on military
      bases, people living on First Nations reserves, institutionalized persons, and households living in the rural areas
      of the three northern territories
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/pub/62-553-x/62-553-x2015001-eng.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: N8c4a27372d53442f97ab645d5b3b3a14
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Household
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianHouseholdsConsumersUniverse
sources:
- id: fibo-source-a06a0301d8
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
  sha256: a06a0301d8cf8f8081904fa368ef17074ae7806ea3c96fa34eb61634f9bc05d6
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
title: Canadian households consumers universe
type: Ontology Class
---

# Canadian households consumers universe

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianHouseholdsConsumersUniverse>

## Definition

a statistical universe consisting of all private households in Canada, with the exception of soldiers on military bases, people living on First Nations reserves, institutionalized persons, and households living in the rural areas of the three northern territories

## Relationships

- **Subclass of**: [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `N8c4a27372d53442f97ab645d5b3b3a14`
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Household](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Household.md)

## Annotations

- **label**: Canadian households consumers universe
- **definition**: a statistical universe consisting of all private households in Canada, with the exception of soldiers on military bases, people living on First Nations reserves, institutionalized persons, and households living in the rural areas of the three northern territories
- **adaptedFrom**: http://www.statcan.gc.ca/pub/62-553-x/62-553-x2015001-eng.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
