---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: PFTS QUOTE DRIVEN
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: QUOTE DRIVEN MARKET IS A TRADING SEGMENT UNDER PFTS STOCK EXCHANGE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: PFTS QUOTE DRIVEN
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.pfts.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/QuoteDrivenMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Kiev.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Kiev
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-PFTS.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-PFTS
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PFTSQUOTEDRIVEN.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PFTSQUOTEDRIVEN
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ukraine
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-PFTQ
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: PFTS QUOTE DRIVEN
type: Ontology Individual
---

# PFTS QUOTE DRIVEN

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-PFTQ>

## Relationships

- **Related to**: [Ukraine](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ukraine>)
- **Related to**: [Kiev](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Kiev.md)
- **Related to**: [Facility-PFTS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-PFTS.md)
- **Related to**: [ServiceProvider-PFTSQUOTEDRIVEN](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PFTSQUOTEDRIVEN.md)

## Annotations

- **label**: PFTS QUOTE DRIVEN
- **note**: QUOTE DRIVEN MARKET IS A TRADING SEGMENT UNDER PFTS STOCK EXCHANGE.
- **hasFormalName**: PFTS QUOTE DRIVEN
- **hasWebsite**: http://www.pfts.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
