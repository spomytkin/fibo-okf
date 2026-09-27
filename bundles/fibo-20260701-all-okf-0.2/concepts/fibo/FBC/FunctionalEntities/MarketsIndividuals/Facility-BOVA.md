---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BOLSA DE CORREDORES - BOLSA DE VALORES
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: EQUITY AND BOND MARKET.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BOLSA DE CORREDORES - BOLSA DE VALORES
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.bovalpo.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Valparaiso.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Valparaiso
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADECORREDORES-BOLSADEVALORES.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADECORREDORES-BOLSADEVALORES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Chile
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BOVA
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BOLSA DE CORREDORES - BOLSA DE VALORES
type: Ontology Individual
---

# BOLSA DE CORREDORES - BOLSA DE VALORES

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BOVA>

## Relationships

- **Related to**: [Chile](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Chile>)
- **Related to**: [Valparaiso](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Valparaiso.md)
- **Related to**: [ServiceProvider-BOLSADECORREDORES-BOLSADEVALORES](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSADECORREDORES-BOLSADEVALORES.md)

## Annotations

- **label**: BOLSA DE CORREDORES - BOLSA DE VALORES
- **note**: EQUITY AND BOND MARKET.
- **hasFormalName**: BOLSA DE CORREDORES - BOLSA DE VALORES
- **hasWebsite**: http://www.bovalpo.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
