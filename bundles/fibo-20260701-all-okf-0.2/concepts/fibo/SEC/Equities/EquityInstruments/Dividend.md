---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: announced commitment to make a specific distribution of a portion of earnings to shareholders, prorated by class
      of security
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The amount and timing of payment is set by the board of directors, typically quarterly. Dividends may be paid in
      the form of money, shares, scrip, or on rare occasion, property.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/DividendSchedule
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentAmount
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/DividendDistributionMethod
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDistributionMethod
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Commitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: dividend
type: Ontology Class
---

# dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend>

## Definition

announced commitment to make a specific distribution of a portion of earnings to shareholders, prorated by class of security

## Relationships

- **Subclass of**: [Commitment](/concepts/fibo/FND/Agreements/Agreements/Commitment.md)

## Constraints

- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: min qualified cardinality 0 of type [DividendSchedule](/concepts/fibo/SEC/Equities/EquityInstruments/DividendSchedule.md)
- **[hasPaymentAmount](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentAmount.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasDistributionMethod](/concepts/fibo/SEC/Equities/EquityInstruments/hasDistributionMethod.md)**: max qualified cardinality 1 of type [DividendDistributionMethod](/concepts/fibo/SEC/Equities/EquityInstruments/DividendDistributionMethod.md)

## Annotations

- **label**: dividend
- **definition**: announced commitment to make a specific distribution of a portion of earnings to shareholders, prorated by class of security
- **explanatoryNote**: The amount and timing of payment is set by the board of directors, typically quarterly. Dividends may be paid in the form of money, shares, scrip, or on rare occasion, property.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
