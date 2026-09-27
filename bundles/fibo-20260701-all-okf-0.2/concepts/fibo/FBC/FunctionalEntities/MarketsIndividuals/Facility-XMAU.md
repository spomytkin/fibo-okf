---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: STOCK EXCHANGE OF MAURITIUS LTD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: STOCK EXCHANGE OF MAURITIUS LTD
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.stockexchangeofmauritius.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Port_Louis.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Port_Louis
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STOCKEXCHANGEOFMAURITIUSLTD.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STOCKEXCHANGEOFMAURITIUSLTD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mauritius
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMAU
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: STOCK EXCHANGE OF MAURITIUS LTD
type: Ontology Individual
---

# STOCK EXCHANGE OF MAURITIUS LTD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMAU>

## Relationships

- **Related to**: [Mauritius](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mauritius>)
- **Related to**: [Port_Louis](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Port_Louis.md)
- **Related to**: [ServiceProvider-STOCKEXCHANGEOFMAURITIUSLTD](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STOCKEXCHANGEOFMAURITIUSLTD.md)

## Annotations

- **label**: STOCK EXCHANGE OF MAURITIUS LTD
- **hasFormalName**: STOCK EXCHANGE OF MAURITIUS LTD
- **hasWebsite**: http://www.stockexchangeofmauritius.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
