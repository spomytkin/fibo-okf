---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CEVALDOM - OTC MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ADMINISTRATOR OF AN OVER THE COUNTER MARKET OPERATIONS REGISTRATION SYSTEM (OTC).
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: CEVALDOM - OTC MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.cevaldom.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Santo_Domingo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Santo_Domingo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-959800BCG62RCSR5H360.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-959800BCG62RCSR5H360
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/DominicanRepublic
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCVD
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: CEVALDOM - OTC MARKET
type: Ontology Individual
---

# CEVALDOM - OTC MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCVD>

## Relationships

- **Related to**: [DominicanRepublic](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/DominicanRepublic>)
- **Related to**: [Santo_Domingo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Santo_Domingo.md)
- **Related to**: [ServiceProvider-L-959800BCG62RCSR5H360](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-959800BCG62RCSR5H360.md)

## Annotations

- **label**: CEVALDOM - OTC MARKET
- **note**: ADMINISTRATOR OF AN OVER THE COUNTER MARKET OPERATIONS REGISTRATION SYSTEM (OTC).
- **hasFormalName**: CEVALDOM - OTC MARKET
- **hasWebsite**: http://www.cevaldom.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
