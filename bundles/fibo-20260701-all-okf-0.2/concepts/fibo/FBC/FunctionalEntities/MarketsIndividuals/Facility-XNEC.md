---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NATIONAL STOCK EXCHANGE OF AUSTRALIA LIMITED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NSXA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NATIONAL STOCK EXCHANGE OF AUSTRALIA LIMITED
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nsxa.com.au
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Newcastle.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Newcastle
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NATIONALSTOCKEXCHANGEOFAUSTRALIALIMITED.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NATIONALSTOCKEXCHANGEOFAUSTRALIALIMITED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNEC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NATIONAL STOCK EXCHANGE OF AUSTRALIA LIMITED
type: Ontology Individual
---

# NATIONAL STOCK EXCHANGE OF AUSTRALIA LIMITED

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNEC>

## Relationships

- **Related to**: [Australia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia>)
- **Related to**: [Newcastle](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Newcastle.md)
- **Related to**: [ServiceProvider-NATIONALSTOCKEXCHANGEOFAUSTRALIALIMITED](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NATIONALSTOCKEXCHANGEOFAUSTRALIALIMITED.md)

## Annotations

- **label**: NATIONAL STOCK EXCHANGE OF AUSTRALIA LIMITED
- **hasFacilityAcronym**: NSXA
- **hasFormalName**: NATIONAL STOCK EXCHANGE OF AUSTRALIA LIMITED
- **hasWebsite**: http://www.nsxa.com.au

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
