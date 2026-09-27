---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NYSE Dark
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: NYSE Dark segment-level market that is a segment of the NYSE involved in trading of dark pools
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NYSEDARK
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NYSE Dark
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.nyse.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DarkPool
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/IntercontinentalExchange.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/IntercontinentalExchange
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  same_as:
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-NYSD.md
    predicate: http://www.w3.org/2002/07/owl#sameAs
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NYSD
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEDark
sources:
- id: fibo-source-7c3670c0b0
  resource: references/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
  sha256: 7c3670c0b01b44daf9d230ebaa0d7ca05831ee5103d2f94eabe7f3b40573ffd1
  title: FIBO source EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
title: NYSE Dark
type: Ontology Individual
---

# NYSE Dark

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEDark>

## Definition

NYSE Dark segment-level market that is a segment of the NYSE involved in trading of dark pools

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [NewYorkStockExchange](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md)
- **Related to**: [IntercontinentalExchange](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/IntercontinentalExchange.md)
- **Same as**: [Facility-NYSD](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-NYSD.md)

## Annotations

- **label**: NYSE Dark
- **definition**: NYSE Dark segment-level market that is a segment of the NYSE involved in trading of dark pools
- **hasFacilityAcronym**: NYSEDARK
- **hasFormalName**: NYSE Dark
- **hasWebsite**: https://www.nyse.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
