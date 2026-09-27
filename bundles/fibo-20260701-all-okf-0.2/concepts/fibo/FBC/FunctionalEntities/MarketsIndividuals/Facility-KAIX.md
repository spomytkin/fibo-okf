---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CBOE JAPAN - KAI-X
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: PURELY BROKER NEUTRAL CROSSING POOL FOR JAPANESE EQUITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: CBOE JAPAN - KAI-X
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.cboe.co.jp
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RecognizedMarketOperator
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-CHIJ.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-CHIJ
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CBOEJAPANLIMITED.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CBOEJAPANLIMITED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Japan
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-KAIX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: CBOE JAPAN - KAI-X
type: Ontology Individual
---

# CBOE JAPAN - KAI-X

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-KAIX>

## Relationships

- **Related to**: [Japan](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Japan>)
- **Related to**: [Tokyo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo.md)
- **Related to**: [Facility-CHIJ](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-CHIJ.md)
- **Related to**: [ServiceProvider-CBOEJAPANLIMITED](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CBOEJAPANLIMITED.md)

## Annotations

- **label**: CBOE JAPAN - KAI-X
- **note**: PURELY BROKER NEUTRAL CROSSING POOL FOR JAPANESE EQUITIES.
- **hasFormalName**: CBOE JAPAN - KAI-X
- **hasWebsite**: http://www.cboe.co.jp

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
