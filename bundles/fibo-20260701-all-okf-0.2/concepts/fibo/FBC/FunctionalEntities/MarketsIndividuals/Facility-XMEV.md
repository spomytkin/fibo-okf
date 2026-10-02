---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MERCADO DE VALORES DE BUENOS AIRES S.A.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: MERVAL
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MERCADO DE VALORES DE BUENOS AIRES S.A.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.merval.sba.com.ar
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Buenos_Aires.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Buenos_Aires
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBUE.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBUE
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEVALORESDEBUENOSAIRESSA.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEVALORESDEBUENOSAIRESSA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Argentina
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMEV
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MERCADO DE VALORES DE BUENOS AIRES S.A.
type: Ontology Individual
---

# MERCADO DE VALORES DE BUENOS AIRES S.A.

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMEV>

## Relationships

- **Related to**: [Argentina](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Argentina>)
- **Related to**: [Buenos_Aires](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Buenos_Aires.md)
- **Related to**: [Facility-XBUE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBUE.md)
- **Related to**: [ServiceProvider-MERCADODEVALORESDEBUENOSAIRESSA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEVALORESDEBUENOSAIRESSA.md)

## Annotations

- **label**: MERCADO DE VALORES DE BUENOS AIRES S.A.
- **hasFacilityAcronym**: MERVAL
- **hasFormalName**: MERCADO DE VALORES DE BUENOS AIRES S.A.
- **hasWebsite**: http://www.merval.sba.com.ar

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
