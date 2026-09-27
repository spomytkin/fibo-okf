---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: explicit contract event schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: schedule of events, including but not limited to payment events, rate reset events and others that will occur over
      the lifetime of the credit agreement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is a schedule of actual dates and events that are terms of the contract.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/AdHocSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AdHocSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ExplicitContractEventSchedule
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: explicit contract event schedule
type: Ontology Class
---

# explicit contract event schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ExplicitContractEventSchedule>

## Definition

schedule of events, including but not limited to payment events, rate reset events and others that will occur over the lifetime of the credit agreement

## Relationships

- **Subclass of**: [AdHocSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/AdHocSchedule.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)

## Annotations

- **label**: explicit contract event schedule
- **definition**: schedule of events, including but not limited to payment events, rate reset events and others that will occur over the lifetime of the credit agreement
- **explanatoryNote**: This is a schedule of actual dates and events that are terms of the contract.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
