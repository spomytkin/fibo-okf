---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Federal Reserve First District
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: jurisdiction of the First District of the Federal Reserve, which covers the New England states of Maine, New Hampshire,
      Vermont, and Massachusetts
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://federalreserve.gov/aboutthefed/directors/map-of-districts.htm
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveDistrict
  related_to:
  - predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasReach
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Maine
  - predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasReach
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Massachusetts
  - predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasReach
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/NewHampshire
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveFirstDistrict
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Federal Reserve First District
type: Ontology Individual
---

# Federal Reserve First District

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveFirstDistrict>

## Definition

jurisdiction of the First District of the Federal Reserve, which covers the New England states of Maine, New Hampshire, Vermont, and Massachusetts

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [Maine](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Maine>)
- **Related to**: [Massachusetts](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Massachusetts>)
- **Related to**: [NewHampshire](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/NewHampshire>)

## Annotations

- **label**: Federal Reserve First District
- **definition**: jurisdiction of the First District of the Federal Reserve, which covers the New England states of Maine, New Hampshire, Vermont, and Massachusetts
- **adaptedFrom**: http://federalreserve.gov/aboutthefed/directors/map-of-districts.htm

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
