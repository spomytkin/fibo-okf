---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: LATIN AMERICAN STOCK EXCHANGE, INC.
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: 'SPANISH: BOLSA LATINOAMERICANA DE VALORES, S.A.'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: LATINEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: LATIN AMERICAN STOCK EXCHANGE, INC.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.latinexbolsa.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Panama_City.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Panama_City
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSALATINOAMERICANADEVALORESSA.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSALATINOAMERICANADEVALORESSA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Panama
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPTY
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: LATIN AMERICAN STOCK EXCHANGE, INC.
type: Ontology Individual
---

# LATIN AMERICAN STOCK EXCHANGE, INC.

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPTY>

## Relationships

- **Related to**: [Panama](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Panama>)
- **Related to**: [Panama_City](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Panama_City.md)
- **Related to**: [ServiceProvider-BOLSALATINOAMERICANADEVALORESSA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BOLSALATINOAMERICANADEVALORESSA.md)

## Annotations

- **label**: LATIN AMERICAN STOCK EXCHANGE, INC.
- **note**: SPANISH: BOLSA LATINOAMERICANA DE VALORES, S.A.
- **hasFacilityAcronym**: LATINEX
- **hasFormalName**: LATIN AMERICAN STOCK EXCHANGE, INC.
- **hasWebsite**: http://www.latinexbolsa.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
