---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: AREX - AUTOMATED RECEIVABLES EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MARKET FOR ETR (EXCHANGE TRADED RECEIVABLES) ORDER EXECUTION.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: AREX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: AREX - AUTOMATED RECEIVABLES EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://arex.io
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-AREX-AUTOMATEDRECEIVABLESEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-AREX-AUTOMATEDRECEIVABLESEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ireland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-AREX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: AREX - AUTOMATED RECEIVABLES EXCHANGE
type: Ontology Individual
---

# AREX - AUTOMATED RECEIVABLES EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-AREX>

## Relationships

- **Related to**: [Ireland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ireland>)
- **Related to**: [Dublin](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin.md)
- **Related to**: [ServiceProvider-AREX-AUTOMATEDRECEIVABLESEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-AREX-AUTOMATEDRECEIVABLESEXCHANGE.md)

## Annotations

- **label**: AREX - AUTOMATED RECEIVABLES EXCHANGE
- **note**: MARKET FOR ETR (EXCHANGE TRADED RECEIVABLES) ORDER EXECUTION.
- **hasFacilityAcronym**: AREX
- **hasFormalName**: AREX - AUTOMATED RECEIVABLES EXCHANGE
- **hasWebsite**: http://arex.io

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
