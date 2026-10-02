---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NASDAQ OMX DERIVATIVES MARKETS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: NASDAQ OMX NORDIC HAVE A MIC (XSTO) THAT SHOULD BE USED FOR REPORTING PURPOSES (INCLUDING THE DERIVATIVES MARKET)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NASDAQ OMX DERIVATIVES MARKETS
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Stockholm.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Stockholm
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSTO.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSTO
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NASDAQOMXDERIVATIVESMARKETS.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NASDAQOMXDERIVATIVESMARKETS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Sweden
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NASN
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NASDAQ OMX DERIVATIVES MARKETS
type: Ontology Individual
---

# NASDAQ OMX DERIVATIVES MARKETS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NASN>

## Relationships

- **Related to**: [Sweden](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Sweden>)
- **Related to**: [Stockholm](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Stockholm.md)
- **Related to**: [Facility-XSTO](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSTO.md)
- **Related to**: [ServiceProvider-NASDAQOMXDERIVATIVESMARKETS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NASDAQOMXDERIVATIVESMARKETS.md)

## Annotations

- **label**: NASDAQ OMX DERIVATIVES MARKETS
- **note**: NASDAQ OMX NORDIC HAVE A MIC (XSTO) THAT SHOULD BE USED FOR REPORTING PURPOSES (INCLUDING THE DERIVATIVES MARKET)
- **hasFormalName**: NASDAQ OMX DERIVATIVES MARKETS

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
