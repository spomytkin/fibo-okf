---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: COLOMBO STOCK EXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: COLOMBO STOCK EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.cse.lk
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Colombo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Colombo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-COLOMBOSTOCKEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-COLOMBOSTOCKEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/SriLanka
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCOL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: COLOMBO STOCK EXCHANGE
type: Ontology Individual
---

# COLOMBO STOCK EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCOL>

## Relationships

- **Related to**: [SriLanka](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/SriLanka>)
- **Related to**: [Colombo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Colombo.md)
- **Related to**: [ServiceProvider-COLOMBOSTOCKEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-COLOMBOSTOCKEXCHANGE.md)

## Annotations

- **label**: COLOMBO STOCK EXCHANGE
- **hasFormalName**: COLOMBO STOCK EXCHANGE
- **hasWebsite**: http://www.cse.lk

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
