---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CBOE EUROPE REGULATED MARKETS (NL)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: CBOE EU RM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: CBOE EUROPE REGULATED MARKETS (NL)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://markets.cboe.com/europe/equities/about/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Amsterdam.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Amsterdam
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2549007JY1TP7I1IMY80.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2549007JY1TP7I1IMY80
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Netherlands
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-CCRM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: CBOE EUROPE REGULATED MARKETS (NL)
type: Ontology Individual
---

# CBOE EUROPE REGULATED MARKETS (NL)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-CCRM>

## Relationships

- **Related to**: [Netherlands](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Netherlands>)
- **Related to**: [Amsterdam](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Amsterdam.md)
- **Related to**: [ServiceProvider-L-2549007JY1TP7I1IMY80](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2549007JY1TP7I1IMY80.md)

## Annotations

- **label**: CBOE EUROPE REGULATED MARKETS (NL)
- **hasFacilityAcronym**: CBOE EU RM
- **hasFormalName**: CBOE EUROPE REGULATED MARKETS (NL)
- **hasWebsite**: http://markets.cboe.com/europe/equities/about/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
