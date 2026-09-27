---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: IBERIAN GAS HUB
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: TRADING PLATFORM FOR THE IBERIAN GAS MARKET.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: IBGH
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: IBERIAN GAS HUB
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.iberiangashub.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bilbao.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Bilbao
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-IBERIANGASHUB.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-IBERIANGASHUB
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Spain
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IBGH
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: IBERIAN GAS HUB
type: Ontology Individual
---

# IBERIAN GAS HUB

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IBGH>

## Relationships

- **Related to**: [Spain](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Spain>)
- **Related to**: [Bilbao](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bilbao.md)
- **Related to**: [ServiceProvider-IBERIANGASHUB](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-IBERIANGASHUB.md)

## Annotations

- **label**: IBERIAN GAS HUB
- **note**: TRADING PLATFORM FOR THE IBERIAN GAS MARKET.
- **hasFacilityAcronym**: IBGH
- **hasFormalName**: IBERIAN GAS HUB
- **hasWebsite**: http://www.iberiangashub.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
