---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: THE INTERNATIONAL STOCK EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGULATED MARKET.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: TISE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: THE INTERNATIONAL STOCK EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.tisegroup.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Peter_Port.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Peter_Port
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2138007LTWIYRO2W8C97.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2138007LTWIYRO2W8C97
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Guernsey
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCIE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: THE INTERNATIONAL STOCK EXCHANGE
type: Ontology Individual
---

# THE INTERNATIONAL STOCK EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCIE>

## Relationships

- **Related to**: [Guernsey](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Guernsey>)
- **Related to**: [Saint_Peter_Port](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Peter_Port.md)
- **Related to**: [ServiceProvider-L-2138007LTWIYRO2W8C97](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2138007LTWIYRO2W8C97.md)

## Annotations

- **label**: THE INTERNATIONAL STOCK EXCHANGE
- **note**: REGULATED MARKET.
- **hasFacilityAcronym**: TISE
- **hasFormalName**: THE INTERNATIONAL STOCK EXCHANGE
- **hasWebsite**: http://www.tisegroup.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
