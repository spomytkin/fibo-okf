---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: AMMAN STOCK EXCHANGE - NON-LISTED SECURITIES MARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: ASE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: AMMAN STOCK EXCHANGE - NON-LISTED SECURITIES MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.exchange.jo
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Amman.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Amman
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XAMM.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XAMM
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-AMMANSTOCKEXCHANGE-NON-LISTEDSECURITIESMARKET.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-AMMANSTOCKEXCHANGE-NON-LISTEDSECURITIESMARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Jordan
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-AMNL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: AMMAN STOCK EXCHANGE - NON-LISTED SECURITIES MARKET
type: Ontology Individual
---

# AMMAN STOCK EXCHANGE - NON-LISTED SECURITIES MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-AMNL>

## Relationships

- **Related to**: [Jordan](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Jordan>)
- **Related to**: [Amman](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Amman.md)
- **Related to**: [Facility-XAMM](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XAMM.md)
- **Related to**: [ServiceProvider-AMMANSTOCKEXCHANGE-NON-LISTEDSECURITIESMARKET](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-AMMANSTOCKEXCHANGE-NON-LISTEDSECURITIESMARKET.md)

## Annotations

- **label**: AMMAN STOCK EXCHANGE - NON-LISTED SECURITIES MARKET
- **hasFacilityAcronym**: ASE
- **hasFormalName**: AMMAN STOCK EXCHANGE - NON-LISTED SECURITIES MARKET
- **hasWebsite**: http://www.exchange.jo

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
