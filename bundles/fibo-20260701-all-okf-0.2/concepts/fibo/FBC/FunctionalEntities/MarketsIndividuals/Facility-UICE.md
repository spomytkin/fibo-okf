---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: UKRAINIAN INTERBANK CURRENCY EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERED MARKET FOR EQUITIES, BONDS AND DERIVATIVES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: UICE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: UKRAINIAN INTERBANK CURRENCY EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.uicegroup.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Kiev.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Kiev
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-894500C5FJGWR7DWUN92.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-894500C5FJGWR7DWUN92
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ukraine
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-UICE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: UKRAINIAN INTERBANK CURRENCY EXCHANGE
type: Ontology Individual
---

# UKRAINIAN INTERBANK CURRENCY EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-UICE>

## Relationships

- **Related to**: [Ukraine](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ukraine>)
- **Related to**: [Kiev](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Kiev.md)
- **Related to**: [ServiceProvider-L-894500C5FJGWR7DWUN92](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-894500C5FJGWR7DWUN92.md)

## Annotations

- **label**: UKRAINIAN INTERBANK CURRENCY EXCHANGE
- **note**: REGISTERED MARKET FOR EQUITIES, BONDS AND DERIVATIVES.
- **hasFacilityAcronym**: UICE
- **hasFormalName**: UKRAINIAN INTERBANK CURRENCY EXCHANGE
- **hasWebsite**: http://www.uicegroup.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
