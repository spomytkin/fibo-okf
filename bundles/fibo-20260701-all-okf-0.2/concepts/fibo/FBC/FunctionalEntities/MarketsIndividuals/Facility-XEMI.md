---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: XETRA MIDPOINT SCALE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: 'MARKET LAUNCH: NOVEMBER 2024.'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: XETRA MIDPOINT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: XETRA MIDPOINT SCALE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://deutsche-boerse.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XETR.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XETR
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-391200OUOEWDQSEJ0Y74.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-391200OUOEWDQSEJ0Y74
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEMI
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: XETRA MIDPOINT SCALE
type: Ontology Individual
---

# XETRA MIDPOINT SCALE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEMI>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Frankfurt](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md)
- **Related to**: [Facility-XETR](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XETR.md)
- **Related to**: [ServiceProvider-L-391200OUOEWDQSEJ0Y74](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-391200OUOEWDQSEJ0Y74.md)

## Annotations

- **label**: XETRA MIDPOINT SCALE
- **note**: MARKET LAUNCH: NOVEMBER 2024.
- **hasFacilityAcronym**: XETRA MIDPOINT
- **hasFormalName**: XETRA MIDPOINT SCALE
- **hasWebsite**: https://deutsche-boerse.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
