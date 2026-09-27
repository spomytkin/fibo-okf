---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: STOXX LIMITED - VOLATILITY INDICES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: STOXX LIMITED - VOLATILITY INDICES
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.stoxx.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Zurich.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Zurich
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-STOX.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-STOX
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STOXXLIMITED-VOLATILITYINDICES.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STOXXLIMITED-VOLATILITYINDICES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSTV
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: STOXX LIMITED - VOLATILITY INDICES
type: Ontology Individual
---

# STOXX LIMITED - VOLATILITY INDICES

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSTV>

## Relationships

- **Related to**: [Switzerland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland>)
- **Related to**: [Zurich](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Zurich.md)
- **Related to**: [Facility-STOX](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-STOX.md)
- **Related to**: [ServiceProvider-STOXXLIMITED-VOLATILITYINDICES](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STOXXLIMITED-VOLATILITYINDICES.md)

## Annotations

- **label**: STOXX LIMITED - VOLATILITY INDICES
- **hasFormalName**: STOXX LIMITED - VOLATILITY INDICES
- **hasWebsite**: http://www.stoxx.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
