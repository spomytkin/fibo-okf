---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BORSA ISTANBUL
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: CHANGE OF MARKET NAME AND MARKET WEBSITE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BORSA ISTANBUL
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.borsaistanbul.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Istanbul.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Istanbul
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BORSAISTANBUL.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BORSAISTANBUL
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Turkey
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XIST
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BORSA ISTANBUL
type: Ontology Individual
---

# BORSA ISTANBUL

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XIST>

## Relationships

- **Related to**: [Turkey](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Turkey>)
- **Related to**: [Istanbul](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Istanbul.md)
- **Related to**: [ServiceProvider-BORSAISTANBUL](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BORSAISTANBUL.md)

## Annotations

- **label**: BORSA ISTANBUL
- **note**: CHANGE OF MARKET NAME AND MARKET WEBSITE
- **hasFormalName**: BORSA ISTANBUL
- **hasWebsite**: http://www.borsaistanbul.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
