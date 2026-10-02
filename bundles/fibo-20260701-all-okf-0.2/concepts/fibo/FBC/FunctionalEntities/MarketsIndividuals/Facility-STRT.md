---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: PRAGUE STOCK EXCHANGE - START (MTF)
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: UNREGULATED MARKET OF THE PRAGUE STOCK EXCHANGE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: PSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: PRAGUE STOCK EXCHANGE - START (MTF)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.pse.cz
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Prague.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Prague
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPRA.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPRA
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-315700KVEWB12APT2364.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-315700KVEWB12APT2364
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Czechia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-STRT
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: PRAGUE STOCK EXCHANGE - START (MTF)
type: Ontology Individual
---

# PRAGUE STOCK EXCHANGE - START (MTF)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-STRT>

## Relationships

- **Related to**: [Czechia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Czechia>)
- **Related to**: [Prague](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Prague.md)
- **Related to**: [Facility-XPRA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPRA.md)
- **Related to**: [ServiceProvider-L-315700KVEWB12APT2364](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-315700KVEWB12APT2364.md)

## Annotations

- **label**: PRAGUE STOCK EXCHANGE - START (MTF)
- **note**: UNREGULATED MARKET OF THE PRAGUE STOCK EXCHANGE.
- **hasFacilityAcronym**: PSE
- **hasFormalName**: PRAGUE STOCK EXCHANGE - START (MTF)
- **hasWebsite**: http://www.pse.cz

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
