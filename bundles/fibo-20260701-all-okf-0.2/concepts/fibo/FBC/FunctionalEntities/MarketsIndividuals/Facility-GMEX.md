---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: GREENMARKET EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: TRADING CEASED AS OF 29TH JUNE 2012. MARKET WILL NOT BE REACTIVATED.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: GREENMARKET EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.greenmarket-exchange.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Munich.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Munich
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-391200Z7ZWISADXEGZ47.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-391200Z7ZWISADXEGZ47
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GMEX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: GREENMARKET EXCHANGE
type: Ontology Individual
---

# GREENMARKET EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GMEX>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Munich](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Munich.md)
- **Related to**: [ServiceProvider-L-391200Z7ZWISADXEGZ47](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-391200Z7ZWISADXEGZ47.md)

## Annotations

- **label**: GREENMARKET EXCHANGE
- **note**: TRADING CEASED AS OF 29TH JUNE 2012. MARKET WILL NOT BE REACTIVATED.
- **hasFormalName**: GREENMARKET EXCHANGE
- **hasWebsite**: http://www.greenmarket-exchange.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
