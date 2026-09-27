---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BLOCK EVENT
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ELECTRONIC BLOCK TRADING PLATFORM FOR EQUITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BLOCK EVENT
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.blockevent.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Melbourne.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Melbourne
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BLOCKEVENT.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BLOCKEVENT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BLEV
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BLOCK EVENT
type: Ontology Individual
---

# BLOCK EVENT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BLEV>

## Relationships

- **Related to**: [Australia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia>)
- **Related to**: [Melbourne](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Melbourne.md)
- **Related to**: [ServiceProvider-BLOCKEVENT](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BLOCKEVENT.md)

## Annotations

- **label**: BLOCK EVENT
- **note**: ELECTRONIC BLOCK TRADING PLATFORM FOR EQUITIES.
- **hasFormalName**: BLOCK EVENT
- **hasWebsite**: http://www.blockevent.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
