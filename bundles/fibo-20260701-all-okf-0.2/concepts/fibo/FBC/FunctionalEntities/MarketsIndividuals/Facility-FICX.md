---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: FINANCIAL INFORMATION CONTRIBUTORS EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: GLOBAL, CLOUD BASED PLATFORM FOR CONTRIBUTORS INFORMATION EXCHANGE IN REAL-TIME.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: FICONEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: FINANCIAL INFORMATION CONTRIBUTORS EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.ficonex.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Rodgau.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Rodgau
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FINANCIALINFORMATIONCONTRIBUTORSEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FINANCIALINFORMATIONCONTRIBUTORSEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FICX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: FINANCIAL INFORMATION CONTRIBUTORS EXCHANGE
type: Ontology Individual
---

# FINANCIAL INFORMATION CONTRIBUTORS EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FICX>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Rodgau](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Rodgau.md)
- **Related to**: [ServiceProvider-FINANCIALINFORMATIONCONTRIBUTORSEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FINANCIALINFORMATIONCONTRIBUTORSEXCHANGE.md)

## Annotations

- **label**: FINANCIAL INFORMATION CONTRIBUTORS EXCHANGE
- **note**: GLOBAL, CLOUD BASED PLATFORM FOR CONTRIBUTORS INFORMATION EXCHANGE IN REAL-TIME.
- **hasFacilityAcronym**: FICONEX
- **hasFormalName**: FINANCIAL INFORMATION CONTRIBUTORS EXCHANGE
- **hasWebsite**: http://www.ficonex.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
