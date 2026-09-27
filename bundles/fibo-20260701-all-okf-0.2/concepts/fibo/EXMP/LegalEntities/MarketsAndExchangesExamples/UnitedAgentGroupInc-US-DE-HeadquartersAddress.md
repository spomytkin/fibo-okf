---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: United Agent Group Inc. US-DE headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters address for the United Agent Group Inc. US-DE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 3411 Silverside Road
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine2
    value: Tatnall Building STE 104
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '19810'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Wilmington.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Wilmington
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  - predicate: https://www.omg.org/spec/Commons/Locations/hasSubdivision
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Delaware
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/UnitedAgentGroupInc-US-DE-HeadquartersAddress
sources:
- id: fibo-source-7c3670c0b0
  resource: references/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
  sha256: 7c3670c0b01b44daf9d230ebaa0d7ca05831ee5103d2f94eabe7f3b40573ffd1
  title: FIBO source EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
title: United Agent Group Inc. US-DE headquarters address
type: Ontology Individual
---

# United Agent Group Inc. US-DE headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/UnitedAgentGroupInc-US-DE-HeadquartersAddress>

## Definition

headquarters address for the United Agent Group Inc. US-DE

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Wilmington](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Wilmington.md)
- **Related to**: [Delaware](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Delaware>)

## Annotations

- **label**: United Agent Group Inc. US-DE headquarters address
- **definition**: headquarters address for the United Agent Group Inc. US-DE
- **hasAddressLine1**: 3411 Silverside Road
- **hasAddressLine2**: Tatnall Building STE 104
- **hasPostalCode**: 19810

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
