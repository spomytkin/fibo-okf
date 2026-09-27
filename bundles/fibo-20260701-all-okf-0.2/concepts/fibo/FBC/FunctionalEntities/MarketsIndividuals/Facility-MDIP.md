---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MEDIP (MTS PORTUGAL SGMR, SA)
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MTS PORTUGAL IS OPERATING AS A DIVISION OF EUROMTS SINCE 30 JUNE 2014
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: MEDIP
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MEDIP (MTS PORTUGAL SGMR, SA)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.mtsportugal.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Lisbon.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Lisbon
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MEDIPMTSPORTUGALSGMRSA.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MEDIPMTSPORTUGALSGMRSA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Portugal
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MDIP
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MEDIP (MTS PORTUGAL SGMR, SA)
type: Ontology Individual
---

# MEDIP (MTS PORTUGAL SGMR, SA)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MDIP>

## Relationships

- **Related to**: [Portugal](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Portugal>)
- **Related to**: [Lisbon](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Lisbon.md)
- **Related to**: [ServiceProvider-MEDIPMTSPORTUGALSGMRSA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MEDIPMTSPORTUGALSGMRSA.md)

## Annotations

- **label**: MEDIP (MTS PORTUGAL SGMR, SA)
- **note**: MTS PORTUGAL IS OPERATING AS A DIVISION OF EUROMTS SINCE 30 JUNE 2014
- **hasFacilityAcronym**: MEDIP
- **hasFormalName**: MEDIP (MTS PORTUGAL SGMR, SA)
- **hasWebsite**: http://www.mtsportugal.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
