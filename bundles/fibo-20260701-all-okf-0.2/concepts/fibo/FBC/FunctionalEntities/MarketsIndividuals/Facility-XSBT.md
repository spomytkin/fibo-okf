---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SGX BOND PRO
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ELECTRONIC TRADING PLATFORM FOR FIXED INCOME SECURITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SGX-BT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SGX BOND PRO
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.sgx.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RecognizedMarketOperator
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSES.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSES
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300L1LYV2VEI08P16.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300L1LYV2VEI08P16
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Singapore
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSBT
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SGX BOND PRO
type: Ontology Individual
---

# SGX BOND PRO

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSBT>

## Relationships

- **Related to**: [Singapore](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Singapore>)
- **Related to**: [Singapore](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore.md)
- **Related to**: [Facility-XSES](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSES.md)
- **Related to**: [ServiceProvider-L-549300L1LYV2VEI08P16](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300L1LYV2VEI08P16.md)

## Annotations

- **label**: SGX BOND PRO
- **note**: ELECTRONIC TRADING PLATFORM FOR FIXED INCOME SECURITIES.
- **hasFacilityAcronym**: SGX-BT
- **hasFormalName**: SGX BOND PRO
- **hasWebsite**: http://www.sgx.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
