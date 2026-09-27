---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dividend schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: payment schedule indicating the dates on which dividends are due to be paid
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RegularSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RegularSchedule
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/DividendSchedule
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: dividend schedule
type: Ontology Class
---

# dividend schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/DividendSchedule>

## Definition

payment schedule indicating the dates on which dividends are due to be paid

## Relationships

- **Subclass of**: [RegularSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RegularSchedule.md)
- **Subclass of**: [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)

## Annotations

- **label**: dividend schedule
- **definition**: payment schedule indicating the dates on which dividends are due to be paid

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
