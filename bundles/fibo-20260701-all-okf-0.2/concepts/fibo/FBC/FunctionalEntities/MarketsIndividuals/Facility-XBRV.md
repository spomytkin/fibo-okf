---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BOURSE REGIONALE DES VALEURS MOBILIERES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: BRVM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BOURSE REGIONALE DES VALEURS MOBILIERES
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.brvm.org
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Abidjan.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Abidjan
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOURSEREGIONALEDESVALEURSMOBILIERES.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOURSEREGIONALEDESVALEURSMOBILIERES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/CoteDIvoire
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBRV
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BOURSE REGIONALE DES VALEURS MOBILIERES
type: Ontology Individual
---

# BOURSE REGIONALE DES VALEURS MOBILIERES

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBRV>

## Relationships

- **Related to**: [CoteDIvoire](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/CoteDIvoire>)
- **Related to**: [Abidjan](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Abidjan.md)
- **Related to**: [ServiceProvider-BOURSEREGIONALEDESVALEURSMOBILIERES](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOURSEREGIONALEDESVALEURSMOBILIERES.md)

## Annotations

- **label**: BOURSE REGIONALE DES VALEURS MOBILIERES
- **hasFacilityAcronym**: BRVM
- **hasFormalName**: BOURSE REGIONALE DES VALEURS MOBILIERES
- **hasWebsite**: http://www.brvm.org

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
