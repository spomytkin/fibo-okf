---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Federal Reserve Board H.15 rate reset time of day
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the time of day that the Federal Reserve Board publishes Selected Interest Rates (Daily) in Schedule H.15
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.federalreserve.gov/releases/h15/
  - predicate: https://www.omg.org/spec/Commons/DatesAndTimes/hasTimeValue
    value: T16:15:00
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/RateResetTimeOfDay
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/NewYorkFederalReserveBusinessDay.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/NewYorkFederalReserveBusinessDay
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasBusinessCenter
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/FederalReserveBoardH.15RateResetTimeOfDay
sources:
- id: fibo-source-0b5fde6ab3
  resource: references/fibo/IND/InterestRates/MarketDataProviders.rdf
  sha256: 0b5fde6ab3fe477e8381e86968420d93073a53e8b18733937a275f845b4e18c4
  title: FIBO source IND/InterestRates/MarketDataProviders.rdf
title: Federal Reserve Board H.15 rate reset time of day
type: Ontology Individual
---

# Federal Reserve Board H.15 rate reset time of day

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/FederalReserveBoardH.15RateResetTimeOfDay>

## Definition

the time of day that the Federal Reserve Board publishes Selected Interest Rates (Daily) in Schedule H.15

## Relationships

- **Related to**: [NewYorkFederalReserveBusinessDay](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/NewYorkFederalReserveBusinessDay.md)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)

## Annotations

- **label**: Federal Reserve Board H.15 rate reset time of day
- **definition**: the time of day that the Federal Reserve Board publishes Selected Interest Rates (Daily) in Schedule H.15
- **adaptedFrom**: https://www.federalreserve.gov/releases/h15/
- **hasTimeValue**: T16:15:00

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
