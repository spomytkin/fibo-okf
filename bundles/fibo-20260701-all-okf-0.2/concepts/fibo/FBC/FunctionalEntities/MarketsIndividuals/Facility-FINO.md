---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: FINRA ORF (TRADE REPORTING FACILITY)
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: OTC REPORTING FACILITY.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: FINRA ORF (TRADE REPORTING FACILITY)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.finra.org
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/SitesAndFacilities/Facility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Washington.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Washington
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900F5GTSJJHGE9287.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900F5GTSJJHGE9287
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINO
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: FINRA ORF (TRADE REPORTING FACILITY)
type: Ontology Individual
---

# FINRA ORF (TRADE REPORTING FACILITY)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINO>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Washington](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Washington.md)
- **Related to**: [Facility-FINR](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR.md)
- **Related to**: [ServiceProvider-L-254900F5GTSJJHGE9287](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900F5GTSJJHGE9287.md)

## Annotations

- **label**: FINRA ORF (TRADE REPORTING FACILITY)
- **note**: OTC REPORTING FACILITY.
- **hasFormalName**: FINRA ORF (TRADE REPORTING FACILITY)
- **hasWebsite**: http://www.finra.org

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
