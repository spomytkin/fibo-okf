---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MERCADO DE VALORES DE ROSARIO S.A.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: MERVAROS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MERCADO DE VALORES DE ROSARIO S.A.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.mervaros.com.ar
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Rosario.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Rosario
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XROS.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XROS
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEVALORESDEROSARIOSA.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEVALORESDEROSARIOSA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Argentina
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XROX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MERCADO DE VALORES DE ROSARIO S.A.
type: Ontology Individual
---

# MERCADO DE VALORES DE ROSARIO S.A.

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XROX>

## Relationships

- **Related to**: [Argentina](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Argentina>)
- **Related to**: [Rosario](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Rosario.md)
- **Related to**: [Facility-XROS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XROS.md)
- **Related to**: [ServiceProvider-MERCADODEVALORESDEROSARIOSA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEVALORESDEROSARIOSA.md)

## Annotations

- **label**: MERCADO DE VALORES DE ROSARIO S.A.
- **hasFacilityAcronym**: MERVAROS
- **hasFormalName**: MERCADO DE VALORES DE ROSARIO S.A.
- **hasWebsite**: http://www.mervaros.com.ar

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
