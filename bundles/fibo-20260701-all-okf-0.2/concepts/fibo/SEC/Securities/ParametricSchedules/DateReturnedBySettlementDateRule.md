---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: date returned by settlement date rule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: calculated date that is determined via a settlement rule
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/SettlementDateRule
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculatedDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/DateReturnedBySettlementDateRule
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: date returned by settlement date rule
type: Ontology Class
---

# date returned by settlement date rule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/DateReturnedBySettlementDateRule>

## Definition

calculated date that is determined via a settlement rule

## Relationships

- **Subclass of**: [CalculatedDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: all values from of type [SettlementDateRule](/concepts/fibo/SEC/Securities/ParametricSchedules/SettlementDateRule.md)

## Annotations

- **label**: date returned by settlement date rule
- **definition**: calculated date that is determined via a settlement rule

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
