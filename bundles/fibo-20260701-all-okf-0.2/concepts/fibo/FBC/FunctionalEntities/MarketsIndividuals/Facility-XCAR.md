---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BOLSA DE VALORES DE CARACAS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BOLSA DE VALORES DE CARACAS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.bolsadecaracas.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Caracas.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Caracas
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-BVCA.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BVCA
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADEVALORESDECARACAS.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADEVALORESDECARACAS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Venezuela
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCAR
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BOLSA DE VALORES DE CARACAS
type: Ontology Individual
---

# BOLSA DE VALORES DE CARACAS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCAR>

## Relationships

- **Related to**: [Venezuela](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Venezuela>)
- **Related to**: [Caracas](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Caracas.md)
- **Related to**: [Facility-BVCA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-BVCA.md)
- **Related to**: [ServiceProvider-BOLSADEVALORESDECARACAS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADEVALORESDECARACAS.md)

## Annotations

- **label**: BOLSA DE VALORES DE CARACAS
- **hasFormalName**: BOLSA DE VALORES DE CARACAS
- **hasWebsite**: http://www.bolsadecaracas.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
