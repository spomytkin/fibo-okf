---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SAINT VINCENT AND THE GRENADINES SECURITIES EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERED MARKET FOR EQUITIES AND BONDS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SVGEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SAINT VINCENT AND THE GRENADINES SECURITIES EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.svgex.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Kingstown.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Kingstown
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-8945001R4JGZRMTLRM44.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-8945001R4JGZRMTLRM44
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/SaintVincentAndTheGrenadines
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SVXI
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SAINT VINCENT AND THE GRENADINES SECURITIES EXCHANGE
type: Ontology Individual
---

# SAINT VINCENT AND THE GRENADINES SECURITIES EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SVXI>

## Relationships

- **Related to**: [SaintVincentAndTheGrenadines](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/SaintVincentAndTheGrenadines>)
- **Related to**: [Kingstown](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Kingstown.md)
- **Related to**: [ServiceProvider-L-8945001R4JGZRMTLRM44](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-8945001R4JGZRMTLRM44.md)

## Annotations

- **label**: SAINT VINCENT AND THE GRENADINES SECURITIES EXCHANGE
- **note**: REGISTERED MARKET FOR EQUITIES AND BONDS.
- **hasFacilityAcronym**: SVGEX
- **hasFormalName**: SAINT VINCENT AND THE GRENADINES SECURITIES EXCHANGE
- **hasWebsite**: http://www.svgex.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
