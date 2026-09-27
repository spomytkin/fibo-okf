---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: EUREX REPO SECLEND MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ET IS NOW OPERATED FROM FRANKFURT (GERMANY)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: EUREX REPO SECLEND MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.eurexrepo.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEUP.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEUP
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900QA7T9JLRFVNN10.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900QA7T9JLRFVNN10
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEUM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: EUREX REPO SECLEND MARKET
type: Ontology Individual
---

# EUREX REPO SECLEND MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEUM>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Frankfurt](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md)
- **Related to**: [Facility-XEUP](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEUP.md)
- **Related to**: [ServiceProvider-L-529900QA7T9JLRFVNN10](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900QA7T9JLRFVNN10.md)

## Annotations

- **label**: EUREX REPO SECLEND MARKET
- **note**: ET IS NOW OPERATED FROM FRANKFURT (GERMANY)
- **hasFormalName**: EUREX REPO SECLEND MARKET
- **hasWebsite**: http://www.eurexrepo.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
