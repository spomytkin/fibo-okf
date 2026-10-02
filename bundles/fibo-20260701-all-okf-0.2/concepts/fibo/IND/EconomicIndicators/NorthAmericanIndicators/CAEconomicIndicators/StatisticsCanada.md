---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Statistics Canada
  - language: fr
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Statistique Canada
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual representing Statistics Canada, a government agency mandated to collect, compile, analyse, abstract
      and publish statistical information relating to the commercial, industrial, financial, social, economic and general
      activities and condition of the people of Canada
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: StatCan
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/eng/about/mandate
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAgency
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/GovernmentOfCanada.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/GovernmentOfCanada
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCoverageArea
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Canada
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/StatisticsCanada
sources:
- id: fibo-source-a06a0301d8
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
  sha256: a06a0301d8cf8f8081904fa368ef17074ae7806ea3c96fa34eb61634f9bc05d6
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
title: Statistics Canada
type: Ontology Individual
---

# Statistics Canada

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/StatisticsCanada>

## Definition

individual representing Statistics Canada, a government agency mandated to collect, compile, analyse, abstract and publish statistical information relating to the commercial, industrial, financial, social, economic and general activities and condition of the people of Canada

## Relationships

- **Related to**: [GovernmentOfCanada](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/GovernmentOfCanada.md)
- **Related to**: [Canada](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Canada>)

## Annotations

- **label** (en): Statistics Canada
- **label** (fr): Statistique Canada
- **definition**: individual representing Statistics Canada, a government agency mandated to collect, compile, analyse, abstract and publish statistical information relating to the commercial, industrial, financial, social, economic and general activities and condition of the people of Canada
- **abbreviation**: StatCan
- **adaptedFrom**: http://www.statcan.gc.ca/eng/about/mandate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
