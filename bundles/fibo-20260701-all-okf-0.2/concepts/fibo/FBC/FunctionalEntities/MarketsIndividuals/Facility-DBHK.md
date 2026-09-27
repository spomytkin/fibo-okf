---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: DEUTSCHE BANK HONG KONG ATS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ALTERNATIVE TRADING SYSTEM FOR TRADING ASIAN EXCHANGE TRADED EQUITY PRODUCTS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: DEUTSCHE BANK HONG KONG ATS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.db.com/hongkong/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Hong_Kong.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Hong_Kong
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DEUTSCHEBANKHONGKONGATS.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DEUTSCHEBANKHONGKONGATS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/HongKong
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBHK
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: DEUTSCHE BANK HONG KONG ATS
type: Ontology Individual
---

# DEUTSCHE BANK HONG KONG ATS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBHK>

## Relationships

- **Related to**: [HongKong](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/HongKong>)
- **Related to**: [Hong_Kong](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Hong_Kong.md)
- **Related to**: [ServiceProvider-DEUTSCHEBANKHONGKONGATS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DEUTSCHEBANKHONGKONGATS.md)

## Annotations

- **label**: DEUTSCHE BANK HONG KONG ATS
- **note**: ALTERNATIVE TRADING SYSTEM FOR TRADING ASIAN EXCHANGE TRADED EQUITY PRODUCTS.
- **hasFormalName**: DEUTSCHE BANK HONG KONG ATS
- **hasWebsite**: http://www.db.com/hongkong/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
