---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: THE GIBRALTAR STOCK EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: EU REGULATED MARKET FOR TECHNICAL LISTINGS IN COLLECTIVE INVESTMENT SCHEMES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: GSX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: THE GIBRALTAR STOCK EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.gsx.gi
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Gibraltar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Gibraltar
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900JYE69H03XHK860.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900JYE69H03XHK860
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Gibraltar
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GSXL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: THE GIBRALTAR STOCK EXCHANGE
type: Ontology Individual
---

# THE GIBRALTAR STOCK EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GSXL>

## Relationships

- **Related to**: [Gibraltar](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Gibraltar>)
- **Related to**: [Gibraltar](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Gibraltar.md)
- **Related to**: [ServiceProvider-L-254900JYE69H03XHK860](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900JYE69H03XHK860.md)

## Annotations

- **label**: THE GIBRALTAR STOCK EXCHANGE
- **note**: EU REGULATED MARKET FOR TECHNICAL LISTINGS IN COLLECTIVE INVESTMENT SCHEMES.
- **hasFacilityAcronym**: GSX
- **hasFormalName**: THE GIBRALTAR STOCK EXCHANGE
- **hasWebsite**: http://www.gsx.gi

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
