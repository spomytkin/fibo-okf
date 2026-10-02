---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: TRADEGATE BERLIN STOCK EXCHANGE - REGULIERTER MARKT
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: TRADEGATE BERLIN STOCK EXCHANGE IS AN OFFICIAL REGULATED STOCK EXCHANGE IN BERLIN/GERMANY FOR SHARES, BONDS, ETFS
      AND FONDS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: TBSX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: TRADEGATE BERLIN STOCK EXCHANGE - REGULIERTER MARKT
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.tradegatebsx.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Berlin.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Berlin
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-TGAT.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-TGAT
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900I8ESNMLCIQ1U62.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900I8ESNMLCIQ1U62
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XGRM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: TRADEGATE BERLIN STOCK EXCHANGE - REGULIERTER MARKT
type: Ontology Individual
---

# TRADEGATE BERLIN STOCK EXCHANGE - REGULIERTER MARKT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XGRM>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Berlin](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Berlin.md)
- **Related to**: [Facility-TGAT](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-TGAT.md)
- **Related to**: [ServiceProvider-L-529900I8ESNMLCIQ1U62](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900I8ESNMLCIQ1U62.md)

## Annotations

- **label**: TRADEGATE BERLIN STOCK EXCHANGE - REGULIERTER MARKT
- **note**: TRADEGATE BERLIN STOCK EXCHANGE IS AN OFFICIAL REGULATED STOCK EXCHANGE IN BERLIN/GERMANY FOR SHARES, BONDS, ETFS AND FONDS.
- **hasFacilityAcronym**: TBSX
- **hasFormalName**: TRADEGATE BERLIN STOCK EXCHANGE - REGULIERTER MARKT
- **hasWebsite**: http://www.tradegatebsx.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
