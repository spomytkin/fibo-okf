---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: INTERACTIVE BROKERS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SYSTEMATIC INTERNALISER.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: IBKR
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: INTERACTIVE BROKERS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.interactivebrokers.ie
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SystematicInternaliser
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5493001B9LDFCQUY9273.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5493001B9LDFCQUY9273
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ireland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IBSI
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: INTERACTIVE BROKERS
type: Ontology Individual
---

# INTERACTIVE BROKERS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IBSI>

## Relationships

- **Related to**: [Ireland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ireland>)
- **Related to**: [Dublin](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin.md)
- **Related to**: [ServiceProvider-L-5493001B9LDFCQUY9273](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5493001B9LDFCQUY9273.md)

## Annotations

- **label**: INTERACTIVE BROKERS
- **note**: SYSTEMATIC INTERNALISER.
- **hasFacilityAcronym**: IBKR
- **hasFormalName**: INTERACTIVE BROKERS
- **hasWebsite**: http://www.interactivebrokers.ie

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
