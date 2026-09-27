---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SYDBANK A/S
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SYSTEMATIC INTERNALISER.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SYDBANK A/S
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.sydbank.dk
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SystematicInternaliser
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Aabenraa.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Aabenraa
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-GP5DT10VX1QRQUKVBK64.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-GP5DT10VX1QRQUKVBK64
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Denmark
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SBSI
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SYDBANK A/S
type: Ontology Individual
---

# SYDBANK A/S

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SBSI>

## Relationships

- **Related to**: [Denmark](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Denmark>)
- **Related to**: [Aabenraa](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Aabenraa.md)
- **Related to**: [ServiceProvider-L-GP5DT10VX1QRQUKVBK64](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-GP5DT10VX1QRQUKVBK64.md)

## Annotations

- **label**: SYDBANK A/S
- **note**: SYSTEMATIC INTERNALISER.
- **hasFormalName**: SYDBANK A/S
- **hasWebsite**: http://www.sydbank.dk

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
