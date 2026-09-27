---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MACQUARIE EXECUTION (AU)
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MACQUARIE SECURITIES DARK POOL FOR TRADING AUSTRALIAN EQUITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MACQUARIE EXECUTION (AU)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.macquarie.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DarkPool
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-ACMHD8HWFMFUIQQ8Y590.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-ACMHD8HWFMFUIQQ8Y590
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MEAU
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MACQUARIE EXECUTION (AU)
type: Ontology Individual
---

# MACQUARIE EXECUTION (AU)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MEAU>

## Relationships

- **Related to**: [Australia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia>)
- **Related to**: [Sydney](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney.md)
- **Related to**: [ServiceProvider-L-ACMHD8HWFMFUIQQ8Y590](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-ACMHD8HWFMFUIQQ8Y590.md)

## Annotations

- **label**: MACQUARIE EXECUTION (AU)
- **note**: MACQUARIE SECURITIES DARK POOL FOR TRADING AUSTRALIAN EQUITIES.
- **hasFormalName**: MACQUARIE EXECUTION (AU)
- **hasWebsite**: http://www.macquarie.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
