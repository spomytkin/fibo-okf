---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate reset schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: regular, contract-specific schedule including the dates on which a rate reset, and corresponding actual rate, is
      recalculated
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateReset
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOccurrence
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateResetSchedule
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: interest rate reset schedule
type: Ontology Class
---

# interest rate reset schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateResetSchedule>

## Definition

regular, contract-specific schedule including the dates on which a rate reset, and corresponding actual rate, is recalculated

## Relationships

- **Subclass of**: [ProjectedContractEventSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)

## Constraints

- **[hasOccurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOccurrence.md)**: some values from of type [InterestRateReset](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestRateReset.md)

## Annotations

- **label**: interest rate reset schedule
- **definition**: regular, contract-specific schedule including the dates on which a rate reset, and corresponding actual rate, is recalculated

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
