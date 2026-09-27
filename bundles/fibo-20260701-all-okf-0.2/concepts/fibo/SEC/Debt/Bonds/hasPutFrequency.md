---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has put frequency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the recurring window of time in which the put feature can be exercised
  domain:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/PutFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutFeature
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasPutFrequency
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has put frequency
type: Ontology Property
---

# has put frequency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasPutFrequency>

## Definition

indicates the recurring window of time in which the put feature can be exercised

## Relationships

- **Domain**: [PutFeature](/concepts/fibo/SEC/Debt/DebtInstruments/PutFeature.md)
- **Range**: [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **Subproperty of**: [hasRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval.md)

## Annotations

- **label**: has put frequency
- **definition**: indicates the recurring window of time in which the put feature can be exercised

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
