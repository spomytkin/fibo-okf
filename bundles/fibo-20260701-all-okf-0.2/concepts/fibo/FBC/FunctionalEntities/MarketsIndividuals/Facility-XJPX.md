---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: JAPAN EXCHANGE GROUP
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: JPX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: JAPAN EXCHANGE GROUP
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.jpx.co.jp
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-353800578ADEGIJTVW07.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-353800578ADEGIJTVW07
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Japan
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XJPX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: JAPAN EXCHANGE GROUP
type: Ontology Individual
---

# JAPAN EXCHANGE GROUP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XJPX>

## Relationships

- **Related to**: [Japan](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Japan>)
- **Related to**: [Tokyo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo.md)
- **Related to**: [ServiceProvider-L-353800578ADEGIJTVW07](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-353800578ADEGIJTVW07.md)

## Annotations

- **label**: JAPAN EXCHANGE GROUP
- **hasFacilityAcronym**: JPX
- **hasFormalName**: JAPAN EXCHANGE GROUP
- **hasWebsite**: http://www.jpx.co.jp

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
