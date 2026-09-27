---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: STATE STREET BANK INTERNATIONAL FX
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: STATE STREET FOREIGN EXCHANGE SYSTEMATIC INTERNALISER.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SSBI
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: STATE STREET BANK INTERNATIONAL FX
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.statestreet.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SystematicInternaliser
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Munich.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Munich
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-SSBI.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SSBI
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-ZMHGNT7ZPKZ3UFZ8EO46.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-ZMHGNT7ZPKZ3UFZ8EO46
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SSBM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: STATE STREET BANK INTERNATIONAL FX
type: Ontology Individual
---

# STATE STREET BANK INTERNATIONAL FX

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SSBM>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Munich](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Munich.md)
- **Related to**: [Facility-SSBI](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-SSBI.md)
- **Related to**: [ServiceProvider-L-ZMHGNT7ZPKZ3UFZ8EO46](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-ZMHGNT7ZPKZ3UFZ8EO46.md)

## Annotations

- **label**: STATE STREET BANK INTERNATIONAL FX
- **note**: STATE STREET FOREIGN EXCHANGE SYSTEMATIC INTERNALISER.
- **hasFacilityAcronym**: SSBI
- **hasFormalName**: STATE STREET BANK INTERNATIONAL FX
- **hasWebsite**: http://www.statestreet.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
