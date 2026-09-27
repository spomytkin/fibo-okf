---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: RBC EUROPE LIMITED
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: EQUITIES BROKER FILL.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: RBC EUROPE LIMITED
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.rbc.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/London
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-TXDSU46SXBWIGJ8G8E98.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-TXDSU46SXBWIGJ8G8E98
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-RBCE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: RBC EUROPE LIMITED
type: Ontology Individual
---

# RBC EUROPE LIMITED

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-RBCE>

## Relationships

- **Related to**: [UnitedKingdomOfGreatBritainAndNorthernIreland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland>)
- **Related to**: [London](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md)
- **Related to**: [ServiceProvider-L-TXDSU46SXBWIGJ8G8E98](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-TXDSU46SXBWIGJ8G8E98.md)

## Annotations

- **label**: RBC EUROPE LIMITED
- **note**: EQUITIES BROKER FILL.
- **hasFormalName**: RBC EUROPE LIMITED
- **hasWebsite**: http://www.rbc.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
