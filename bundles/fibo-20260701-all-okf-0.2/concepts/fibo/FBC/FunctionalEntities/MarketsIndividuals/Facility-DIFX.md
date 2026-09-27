---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NASDAQ DUBAI
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ON TUESDAY 18TH NOVEMBER, 2008, THE DUBAI INTERNATIONAL FINANCIAL MARKET WAS REBRANDED AS NASDAQ DUBAI.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NDXB
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NASDAQ DUBAI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nasdaqdubai.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dubai.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Dubai
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800QL3V1PYPQMLU38.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800QL3V1PYPQMLU38
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedArabEmirates
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DIFX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NASDAQ DUBAI
type: Ontology Individual
---

# NASDAQ DUBAI

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DIFX>

## Relationships

- **Related to**: [UnitedArabEmirates](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedArabEmirates>)
- **Related to**: [Dubai](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dubai.md)
- **Related to**: [ServiceProvider-L-213800QL3V1PYPQMLU38](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800QL3V1PYPQMLU38.md)

## Annotations

- **label**: NASDAQ DUBAI
- **note**: ON TUESDAY 18TH NOVEMBER, 2008, THE DUBAI INTERNATIONAL FINANCIAL MARKET WAS REBRANDED AS NASDAQ DUBAI.
- **hasFacilityAcronym**: NDXB
- **hasFormalName**: NASDAQ DUBAI
- **hasWebsite**: http://www.nasdaqdubai.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
