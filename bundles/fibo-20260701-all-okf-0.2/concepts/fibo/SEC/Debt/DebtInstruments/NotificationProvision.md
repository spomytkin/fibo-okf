---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: notification provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: provision of a redemption feature defining notification requirements
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/NotificationProvision
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: notification provision
type: Ontology Class
---

# notification provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/NotificationProvision>

## Definition

provision of a redemption feature defining notification requirements

## Relationships

- **Subclass of**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)

## Constraints

- **[hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)**: all values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label**: notification provision
- **definition**: provision of a redemption feature defining notification requirements

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
