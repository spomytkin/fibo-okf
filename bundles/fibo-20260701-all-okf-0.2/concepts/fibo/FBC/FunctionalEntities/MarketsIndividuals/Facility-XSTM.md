---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: FIDELITY CROSSSTREAM ATS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERED ATS FOR TRADING US EQUITIES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: FIDELITY CROSSSTREAM ATS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.capitalmarkets.fidelity.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Boston.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Boston
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-NFSC.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NFSC
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FIDELITYCROSSSTREAMATS.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FIDELITYCROSSSTREAMATS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSTM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: FIDELITY CROSSSTREAM ATS
type: Ontology Individual
---

# FIDELITY CROSSSTREAM ATS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSTM>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Boston](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Boston.md)
- **Related to**: [Facility-NFSC](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-NFSC.md)
- **Related to**: [ServiceProvider-FIDELITYCROSSSTREAMATS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-FIDELITYCROSSSTREAMATS.md)

## Annotations

- **label**: FIDELITY CROSSSTREAM ATS
- **note**: REGISTERED ATS FOR TRADING US EQUITIES
- **hasFormalName**: FIDELITY CROSSSTREAM ATS
- **hasWebsite**: http://www.capitalmarkets.fidelity.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
