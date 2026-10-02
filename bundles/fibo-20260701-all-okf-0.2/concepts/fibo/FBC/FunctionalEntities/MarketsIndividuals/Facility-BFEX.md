---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BAHRAIN FINANCIAL EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: THE BFX IS THE FIRST MULTI-ASSET CLASS EXCHANGE IN THE MIDDLE EAST REGION AND WILL BE INTERNATIONALLY ACCESSIBLE
      TO TRADE CASH INSTRUMENTS, STRUCTURED PRODUCTS AND SHARIA-COMPLIANT FINANCIAL INSTRUMENTS AS WELL AS DERIVATIVES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BAHRAIN FINANCIAL EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.bfx.bh
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Manama.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Manama
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300E7XSMTIA5ORC60.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300E7XSMTIA5ORC60
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Bahrain
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BFEX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BAHRAIN FINANCIAL EXCHANGE
type: Ontology Individual
---

# BAHRAIN FINANCIAL EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BFEX>

## Relationships

- **Related to**: [Bahrain](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Bahrain>)
- **Related to**: [Manama](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Manama.md)
- **Related to**: [ServiceProvider-L-549300E7XSMTIA5ORC60](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300E7XSMTIA5ORC60.md)

## Annotations

- **label**: BAHRAIN FINANCIAL EXCHANGE
- **note**: THE BFX IS THE FIRST MULTI-ASSET CLASS EXCHANGE IN THE MIDDLE EAST REGION AND WILL BE INTERNATIONALLY ACCESSIBLE TO TRADE CASH INSTRUMENTS, STRUCTURED PRODUCTS AND SHARIA-COMPLIANT FINANCIAL INSTRUMENTS AS WELL AS DERIVATIVES.
- **hasFormalName**: BAHRAIN FINANCIAL EXCHANGE
- **hasWebsite**: http://www.bfx.bh

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
