---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BOLSA DE COMERCIO DE CORDOBA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BOLSA DE COMERCIO DE CORDOBA
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.bolsacba.com.ar
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Cordoba.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Cordoba
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADECOMERCIODECORDOBA.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADECOMERCIODECORDOBA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Argentina
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBCC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BOLSA DE COMERCIO DE CORDOBA
type: Ontology Individual
---

# BOLSA DE COMERCIO DE CORDOBA

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBCC>

## Relationships

- **Related to**: [Argentina](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Argentina>)
- **Related to**: [Cordoba](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Cordoba.md)
- **Related to**: [ServiceProvider-BOLSADECOMERCIODECORDOBA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADECOMERCIODECORDOBA.md)

## Annotations

- **label**: BOLSA DE COMERCIO DE CORDOBA
- **hasFormalName**: BOLSA DE COMERCIO DE CORDOBA
- **hasWebsite**: http://www.bolsacba.com.ar

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
