---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: FINEX (NEW YORK AND DUBLIN)
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: FINEX, THEY NO LONGER OPERATE IN DUBLIN AND THEREFORE THE MIC CODE DELETED. FINEX (NOW ICE) CONTINUE TO OPERATE
      AS ICE IN NEW YORK.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: FINEX (NEW YORK AND DUBLIN)
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FINEXNEWYORKANDDUBLIN.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FINEXNEWYORKANDDUBLIN
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ireland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XFNX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: FINEX (NEW YORK AND DUBLIN)
type: Ontology Individual
---

# FINEX (NEW YORK AND DUBLIN)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XFNX>

## Relationships

- **Related to**: [Ireland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ireland>)
- **Related to**: [Dublin](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin.md)
- **Related to**: [ServiceProvider-FINEXNEWYORKANDDUBLIN](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FINEXNEWYORKANDDUBLIN.md)

## Annotations

- **label**: FINEX (NEW YORK AND DUBLIN)
- **note**: FINEX, THEY NO LONGER OPERATE IN DUBLIN AND THEREFORE THE MIC CODE DELETED. FINEX (NOW ICE) CONTINUE TO OPERATE AS ICE IN NEW YORK.
- **hasFormalName**: FINEX (NEW YORK AND DUBLIN)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
