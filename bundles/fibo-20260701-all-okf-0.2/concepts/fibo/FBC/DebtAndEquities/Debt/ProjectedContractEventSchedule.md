---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: projected contract event schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: schedule of events, including but not limited to anticipated payment events, rate reset events and others that
      are expected to occur over the lifetime of the contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A projected schedule is a regular schedule that documents the anchor dates and frequency of occurrences, using
      rules, rather than providing an explicit list of dates. This method will project future event dates (transaction event
      dates), based on the frequencies specified and may be adjusted due to calendar restrictions and other rules to deal
      with holidays, weekends, and so forth in addition to contract-specific events.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasAnticipatedNumberOfPayments
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RegularSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RegularSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: projected contract event schedule
type: Ontology Class
---

# projected contract event schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule>

## Definition

schedule of events, including but not limited to anticipated payment events, rate reset events and others that are expected to occur over the lifetime of the contract

## Relationships

- **Subclass of**: [RegularSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RegularSchedule.md)

## Constraints

- **[hasAnticipatedNumberOfPayments](/concepts/fibo/FBC/DebtAndEquities/Debt/hasAnticipatedNumberOfPayments.md)**: min qualified cardinality 0
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: min qualified cardinality 0 of type [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)

## Annotations

- **label**: projected contract event schedule
- **definition**: schedule of events, including but not limited to anticipated payment events, rate reset events and others that are expected to occur over the lifetime of the contract
- **explanatoryNote**: A projected schedule is a regular schedule that documents the anchor dates and frequency of occurrences, using rules, rather than providing an explicit list of dates. This method will project future event dates (transaction event dates), based on the frequencies specified and may be adjusted due to calendar restrictions and other rules to deal with holidays, weekends, and so forth in addition to contract-specific events.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
