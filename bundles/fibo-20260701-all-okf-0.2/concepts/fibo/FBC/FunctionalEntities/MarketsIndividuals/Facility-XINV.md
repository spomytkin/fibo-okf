---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: INVESTRO
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SETTLEMENT PLATFORM FOR CSD AND NON CSD FUNDS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: INVESTRO
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.investro.de
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900NA0B4IRY21VH50.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900NA0B4IRY21VH50
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XINV
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: INVESTRO
type: Ontology Individual
---

# INVESTRO

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XINV>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Frankfurt](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md)
- **Related to**: [ServiceProvider-L-529900NA0B4IRY21VH50](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900NA0B4IRY21VH50.md)

## Annotations

- **label**: INVESTRO
- **note**: SETTLEMENT PLATFORM FOR CSD AND NON CSD FUNDS.
- **hasFormalName**: INVESTRO
- **hasWebsite**: http://www.investro.de

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
