---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MOZAMBIQUE STOCK EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERED MARKET FOR EQUITIES, BONDS, COMMERCIAL PAPER AND OTHER FINANCIAL INSTRUMENTS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: BVM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MOZAMBIQUE STOCK EXCHANGE
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Maputo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Maputo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MOZAMBIQUESTOCKEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MOZAMBIQUESTOCKEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mozambique
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBVM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MOZAMBIQUE STOCK EXCHANGE
type: Ontology Individual
---

# MOZAMBIQUE STOCK EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBVM>

## Relationships

- **Related to**: [Mozambique](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mozambique>)
- **Related to**: [Maputo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Maputo.md)
- **Related to**: [ServiceProvider-MOZAMBIQUESTOCKEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MOZAMBIQUESTOCKEXCHANGE.md)

## Annotations

- **label**: MOZAMBIQUE STOCK EXCHANGE
- **note**: REGISTERED MARKET FOR EQUITIES, BONDS, COMMERCIAL PAPER AND OTHER FINANCIAL INSTRUMENTS.
- **hasFacilityAcronym**: BVM
- **hasFormalName**: MOZAMBIQUE STOCK EXCHANGE

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
