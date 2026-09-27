---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MERCADO DE FUTUROS DE ACEITE DE OLIVA, S.A.
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MARKET IS CLOSED.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: MFAO
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MERCADO DE FUTUROS DE ACEITE DE OLIVA, S.A.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.mfao.es
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jaen.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Jaen
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEFUTUROSDEACEITEDEOLIVASA.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEFUTUROSDEACEITEDEOLIVASA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Spain
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSRM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MERCADO DE FUTUROS DE ACEITE DE OLIVA, S.A.
type: Ontology Individual
---

# MERCADO DE FUTUROS DE ACEITE DE OLIVA, S.A.

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSRM>

## Relationships

- **Related to**: [Spain](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Spain>)
- **Related to**: [Jaen](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jaen.md)
- **Related to**: [ServiceProvider-MERCADODEFUTUROSDEACEITEDEOLIVASA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MERCADODEFUTUROSDEACEITEDEOLIVASA.md)

## Annotations

- **label**: MERCADO DE FUTUROS DE ACEITE DE OLIVA, S.A.
- **note**: MARKET IS CLOSED.
- **hasFacilityAcronym**: MFAO
- **hasFormalName**: MERCADO DE FUTUROS DE ACEITE DE OLIVA, S.A.
- **hasWebsite**: http://www.mfao.es

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
