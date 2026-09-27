---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NIBC
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SYSTEMATIC INTERNALISER.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NIBC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nibc.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SystematicInternaliser
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/The_Hague.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/The_Hague
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-B64D6Y3LBJS4ANNPCU93.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-B64D6Y3LBJS4ANNPCU93
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Netherlands
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NIBC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NIBC
type: Ontology Individual
---

# NIBC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NIBC>

## Relationships

- **Related to**: [Netherlands](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Netherlands>)
- **Related to**: [The_Hague](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/The_Hague.md)
- **Related to**: [ServiceProvider-L-B64D6Y3LBJS4ANNPCU93](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-B64D6Y3LBJS4ANNPCU93.md)

## Annotations

- **label**: NIBC
- **note**: SYSTEMATIC INTERNALISER.
- **hasFormalName**: NIBC
- **hasWebsite**: http://www.nibc.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
