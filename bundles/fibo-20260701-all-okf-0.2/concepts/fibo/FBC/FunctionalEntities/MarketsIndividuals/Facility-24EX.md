---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: 24 EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: FOREIGN EXCHANGE AND EQUITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: 24EX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: 24 EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.24exchange.net
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bermuda.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Bermuda
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800YXBUZH7G3NDC51.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800YXBUZH7G3NDC51
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Bermuda
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-24EX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: 24 EXCHANGE
type: Ontology Individual
---

# 24 EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-24EX>

## Relationships

- **Related to**: [Bermuda](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Bermuda>)
- **Related to**: [Bermuda](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bermuda.md)
- **Related to**: [ServiceProvider-L-213800YXBUZH7G3NDC51](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800YXBUZH7G3NDC51.md)

## Annotations

- **label**: 24 EXCHANGE
- **note**: FOREIGN EXCHANGE AND EQUITIES.
- **hasFacilityAcronym**: 24EX
- **hasFormalName**: 24 EXCHANGE
- **hasWebsite**: http://www.24exchange.net

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
