---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: OSLO CONNECT
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MULTILATERAL TRADING FACILITY FOR FINANCIAL INSTRUMENTS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: OSLO CONNECT
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.oslobors.no
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Oslo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Oslo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XOSL.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XOSL
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-OSLOCONNECT.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-OSLOCONNECT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Norway
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XOSC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: OSLO CONNECT
type: Ontology Individual
---

# OSLO CONNECT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XOSC>

## Relationships

- **Related to**: [Norway](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Norway>)
- **Related to**: [Oslo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Oslo.md)
- **Related to**: [Facility-XOSL](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XOSL.md)
- **Related to**: [ServiceProvider-OSLOCONNECT](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-OSLOCONNECT.md)

## Annotations

- **label**: OSLO CONNECT
- **note**: MULTILATERAL TRADING FACILITY FOR FINANCIAL INSTRUMENTS
- **hasFormalName**: OSLO CONNECT
- **hasWebsite**: http://www.oslobors.no

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
