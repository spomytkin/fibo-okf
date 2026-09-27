---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: KABU.COMPTS-VWAP
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MARKET HAS CLOSED IN SEPTEMBER 2011
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: KABU.COMPTS-VWAP
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.kabu.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-KABU.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-KABU
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-MB56QSRJ3E5ZE1TK5Y54.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-MB56QSRJ3E5ZE1TK5Y54
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Japan
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-VKAB
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: KABU.COMPTS-VWAP
type: Ontology Individual
---

# KABU.COMPTS-VWAP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-VKAB>

## Relationships

- **Related to**: [Japan](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Japan>)
- **Related to**: [Tokyo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo.md)
- **Related to**: [Facility-KABU](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-KABU.md)
- **Related to**: [ServiceProvider-L-MB56QSRJ3E5ZE1TK5Y54](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-MB56QSRJ3E5ZE1TK5Y54.md)

## Annotations

- **label**: KABU.COMPTS-VWAP
- **note**: MARKET HAS CLOSED IN SEPTEMBER 2011
- **hasFormalName**: KABU.COMPTS-VWAP
- **hasWebsite**: http://www.kabu.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
