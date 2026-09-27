---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CHI-X CANADA ATS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MARKET MODEL FOCUSED ON EQUAL OPPORTUNITY TRADING AND MARKET-LEVEL INNOVATION TO DRIVE GROWTH IN THE CANADIAN EQUITY
      MARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: CHI-X CANADA ATS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.chi-xcanada.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Toronto.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Toronto
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CHI-XCANADAATS.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CHI-XCANADAATS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Canada
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-CHIC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: CHI-X CANADA ATS
type: Ontology Individual
---

# CHI-X CANADA ATS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-CHIC>

## Relationships

- **Related to**: [Canada](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Canada>)
- **Related to**: [Toronto](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Toronto.md)
- **Related to**: [ServiceProvider-CHI-XCANADAATS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CHI-XCANADAATS.md)

## Annotations

- **label**: CHI-X CANADA ATS
- **note**: MARKET MODEL FOCUSED ON EQUAL OPPORTUNITY TRADING AND MARKET-LEVEL INNOVATION TO DRIVE GROWTH IN THE CANADIAN EQUITY MARKET
- **hasFormalName**: CHI-X CANADA ATS
- **hasWebsite**: http://www.chi-xcanada.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
