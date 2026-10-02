---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NILE STOCK EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: THE EGYPTIAN EXCHANGE (EGX) LAUNCHED ON THURSDAY 3 JUNE 2010 THE FIRST TRADING SESSION IN THE NILE STOCK EXCHANGE
      (NILEX).
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NILE STOCK EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nilex.egyptse.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Cairo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Cairo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NILESTOCKEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NILESTOCKEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Egypt
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NILX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NILE STOCK EXCHANGE
type: Ontology Individual
---

# NILE STOCK EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NILX>

## Relationships

- **Related to**: [Egypt](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Egypt>)
- **Related to**: [Cairo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Cairo.md)
- **Related to**: [ServiceProvider-NILESTOCKEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NILESTOCKEXCHANGE.md)

## Annotations

- **label**: NILE STOCK EXCHANGE
- **note**: THE EGYPTIAN EXCHANGE (EGX) LAUNCHED ON THURSDAY 3 JUNE 2010 THE FIRST TRADING SESSION IN THE NILE STOCK EXCHANGE (NILEX).
- **hasFormalName**: NILE STOCK EXCHANGE
- **hasWebsite**: http://www.nilex.egyptse.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
