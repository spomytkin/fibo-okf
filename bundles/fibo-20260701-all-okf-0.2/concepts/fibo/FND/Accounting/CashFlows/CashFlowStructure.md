---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cash flow structure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the structure related to one or more cash flows
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Cash flow structures may involve not only cash flows, but the kind of schedule, historic payments, projected payments,
      a link or links to the relevant contract(s) or account(s), and possibly some triggering event.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlow
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/TriggeringEvent
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlowStructure
sources:
- id: fibo-source-11f30e320a
  resource: references/fibo/FND/Accounting/CashFlows.rdf
  sha256: 11f30e320a47607eb0377d4c97d55d7f8607ad5ba323af00057df476c78573e2
  title: FIBO source FND/Accounting/CashFlows.rdf
title: cash flow structure
type: Ontology Class
---

# cash flow structure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlowStructure>

## Definition

the structure related to one or more cash flows

## Relationships

- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: max qualified cardinality 1 of type [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [CashFlow](/concepts/fibo/FND/Accounting/CashFlows/CashFlow.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: min qualified cardinality 0 of type [TriggeringEvent](/concepts/fibo/FND/Accounting/CashFlows/TriggeringEvent.md)

## Annotations

- **label**: cash flow structure
- **definition**: the structure related to one or more cash flows
- **explanatoryNote**: Cash flow structures may involve not only cash flows, but the kind of schedule, historic payments, projected payments, a link or links to the relevant contract(s) or account(s), and possibly some triggering event.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
