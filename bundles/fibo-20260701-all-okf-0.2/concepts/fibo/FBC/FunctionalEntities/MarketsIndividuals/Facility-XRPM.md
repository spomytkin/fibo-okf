---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ROMANIAN POWER MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ROMANIAN POWER MARKET OPERATOR (OPCOM).
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: ROMANIAN POWER MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.opcom.ro
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bucharest.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Bucharest
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ROMANIANPOWERMARKET.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ROMANIANPOWERMARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Romania
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XRPM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: ROMANIAN POWER MARKET
type: Ontology Individual
---

# ROMANIAN POWER MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XRPM>

## Relationships

- **Related to**: [Romania](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Romania>)
- **Related to**: [Bucharest](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bucharest.md)
- **Related to**: [ServiceProvider-ROMANIANPOWERMARKET](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ROMANIANPOWERMARKET.md)

## Annotations

- **label**: ROMANIAN POWER MARKET
- **note**: ROMANIAN POWER MARKET OPERATOR (OPCOM).
- **hasFormalName**: ROMANIAN POWER MARKET
- **hasWebsite**: http://www.opcom.ro

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
