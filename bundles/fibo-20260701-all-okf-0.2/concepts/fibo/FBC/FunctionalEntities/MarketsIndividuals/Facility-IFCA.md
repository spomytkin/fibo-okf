---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ICE FUTURES CANADA
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ELECTRONIC PLATFORM TO TRADE FUTURES AND OPTIONS PRODUCTS. IFCA REPLACES MIC XWCE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: ICE FUTURES CANADA
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.theice.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Winnipeg.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Winnipeg
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ICEFUTURESCANADA.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ICEFUTURESCANADA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Canada
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IFCA
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: ICE FUTURES CANADA
type: Ontology Individual
---

# ICE FUTURES CANADA

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IFCA>

## Relationships

- **Related to**: [Canada](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Canada>)
- **Related to**: [Winnipeg](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Winnipeg.md)
- **Related to**: [ServiceProvider-ICEFUTURESCANADA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ICEFUTURESCANADA.md)

## Annotations

- **label**: ICE FUTURES CANADA
- **note**: ELECTRONIC PLATFORM TO TRADE FUTURES AND OPTIONS PRODUCTS. IFCA REPLACES MIC XWCE.
- **hasFormalName**: ICE FUTURES CANADA
- **hasWebsite**: http://www.theice.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
