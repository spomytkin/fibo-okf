---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: observed indicator value structure
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection of observations for some key performance indicator measured over a specified window of time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValue
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculationPeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValueStructure
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: observed indicator value structure
type: Ontology Class
---

# observed indicator value structure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValueStructure>

## Definition

collection of observations for some key performance indicator measured over a specified window of time

## Relationships

- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [ObservedIndicatorValue](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValue.md)
- **[hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)**: some values from of type [CalculationPeriod](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculationPeriod.md)

## Annotations

- **label** (en): observed indicator value structure
- **definition** (en): collection of observations for some key performance indicator measured over a specified window of time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
