---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BOURSE AFRICA LIMITED
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MULTI-ASSET CLASS EXCHANGE PROVIDING AN ELECTRONIC PLATFORM FOR TRADING ON COMMODITY DERIVATIVES, CURRENCY DERIVATIVES,
      EQUITY, EQUITY DERIVATIVES AND BONDS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: BAFR
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BOURSE AFRICA LIMITED
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.bourseafrica.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Ebene.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Ebene
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOURSEAFRICALIMITED.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOURSEAFRICALIMITED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mauritius
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GBOT
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BOURSE AFRICA LIMITED
type: Ontology Individual
---

# BOURSE AFRICA LIMITED

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GBOT>

## Relationships

- **Related to**: [Mauritius](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mauritius>)
- **Related to**: [Ebene](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Ebene.md)
- **Related to**: [ServiceProvider-BOURSEAFRICALIMITED](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOURSEAFRICALIMITED.md)

## Annotations

- **label**: BOURSE AFRICA LIMITED
- **note**: MULTI-ASSET CLASS EXCHANGE PROVIDING AN ELECTRONIC PLATFORM FOR TRADING ON COMMODITY DERIVATIVES, CURRENCY DERIVATIVES, EQUITY, EQUITY DERIVATIVES AND BONDS.
- **hasFacilityAcronym**: BAFR
- **hasFormalName**: BOURSE AFRICA LIMITED
- **hasWebsite**: http://www.bourseafrica.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
