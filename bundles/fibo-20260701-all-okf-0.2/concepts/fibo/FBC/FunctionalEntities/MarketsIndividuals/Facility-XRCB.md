---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: RAIFFEISEN CENTROBANK AG
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SYSTEMATIC INTERNALISER. DEMERGER BY ABSORBTION OF THE DIVISION CERTIFICATES AND EQUITY TRADING OF RAIFFEISEN CENTROBANK
      AG TO RAIFFEISEN BANK INTERNATIONAL AG ON 01 DECEMBER 2022.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: RCB
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: RAIFFEISEN CENTROBANK AG
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.rcb.at
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SystematicInternaliser
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Vienna.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Vienna
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900M2F7D5795H1A49.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900M2F7D5795H1A49
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Austria
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XRCB
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: RAIFFEISEN CENTROBANK AG
type: Ontology Individual
---

# RAIFFEISEN CENTROBANK AG

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XRCB>

## Relationships

- **Related to**: [Austria](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Austria>)
- **Related to**: [Vienna](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Vienna.md)
- **Related to**: [ServiceProvider-L-529900M2F7D5795H1A49](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900M2F7D5795H1A49.md)

## Annotations

- **label**: RAIFFEISEN CENTROBANK AG
- **note**: SYSTEMATIC INTERNALISER. DEMERGER BY ABSORBTION OF THE DIVISION CERTIFICATES AND EQUITY TRADING OF RAIFFEISEN CENTROBANK AG TO RAIFFEISEN BANK INTERNATIONAL AG ON 01 DECEMBER 2022.
- **hasFacilityAcronym**: RCB
- **hasFormalName**: RAIFFEISEN CENTROBANK AG
- **hasWebsite**: http://www.rcb.at

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
