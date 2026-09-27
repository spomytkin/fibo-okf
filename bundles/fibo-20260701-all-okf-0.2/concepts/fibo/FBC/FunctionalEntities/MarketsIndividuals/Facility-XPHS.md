---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: PHILIPPINE STOCK EXCHANGE, INC.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: PSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: PHILIPPINE STOCK EXCHANGE, INC.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.pse.com.ph
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Pasig_City.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Pasig_City
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PHILIPPINESTOCKEXCHANGEINC.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PHILIPPINESTOCKEXCHANGEINC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Philippines
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPHS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: PHILIPPINE STOCK EXCHANGE, INC.
type: Ontology Individual
---

# PHILIPPINE STOCK EXCHANGE, INC.

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPHS>

## Relationships

- **Related to**: [Philippines](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Philippines>)
- **Related to**: [Pasig_City](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Pasig_City.md)
- **Related to**: [ServiceProvider-PHILIPPINESTOCKEXCHANGEINC](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PHILIPPINESTOCKEXCHANGEINC.md)

## Annotations

- **label**: PHILIPPINE STOCK EXCHANGE, INC.
- **hasFacilityAcronym**: PSE
- **hasFormalName**: PHILIPPINE STOCK EXCHANGE, INC.
- **hasWebsite**: http://www.pse.com.ph

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
