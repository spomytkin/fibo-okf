---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: LA BOLSA ELECTRONICA DE CHILE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: BOLCHILE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: LA BOLSA ELECTRONICA DE CHILE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.bolchile.cl
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Santiago.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Santiago
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-LABOLSAELECTRONICADECHILE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-LABOLSAELECTRONICADECHILE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Chile
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBCL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: LA BOLSA ELECTRONICA DE CHILE
type: Ontology Individual
---

# LA BOLSA ELECTRONICA DE CHILE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBCL>

## Relationships

- **Related to**: [Chile](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Chile>)
- **Related to**: [Santiago](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Santiago.md)
- **Related to**: [ServiceProvider-LABOLSAELECTRONICADECHILE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-LABOLSAELECTRONICADECHILE.md)

## Annotations

- **label**: LA BOLSA ELECTRONICA DE CHILE
- **hasFacilityAcronym**: BOLCHILE
- **hasFormalName**: LA BOLSA ELECTRONICA DE CHILE
- **hasWebsite**: http://www.bolchile.cl

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
