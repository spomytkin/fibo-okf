---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: FINSTREET GLOBAL MARKETS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: FGM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: FINSTREET GLOBAL MARKETS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.finstreet.ae
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Abu_Dhabi.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Abu_Dhabi
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-984500CCC5DB85F00930.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-984500CCC5DB85F00930
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedArabEmirates
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FGML
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: FINSTREET GLOBAL MARKETS
type: Ontology Individual
---

# FINSTREET GLOBAL MARKETS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FGML>

## Relationships

- **Related to**: [UnitedArabEmirates](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedArabEmirates>)
- **Related to**: [Abu_Dhabi](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Abu_Dhabi.md)
- **Related to**: [ServiceProvider-L-984500CCC5DB85F00930](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-984500CCC5DB85F00930.md)

## Annotations

- **label**: FINSTREET GLOBAL MARKETS
- **hasFacilityAcronym**: FGM
- **hasFormalName**: FINSTREET GLOBAL MARKETS
- **hasWebsite**: http://www.finstreet.ae

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
