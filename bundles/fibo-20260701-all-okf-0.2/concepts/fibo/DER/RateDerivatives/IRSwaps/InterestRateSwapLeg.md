---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate swap leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap leg that has an interest rate payment stream, including both a parametric and cashflow representation for
      the stream of payments
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: interest rate swap stream
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessRecurrenceIntervalConvention
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepSchedule
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentSchedule
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/specifies
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestCalculationSchedule
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/RateBasedLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RateBasedLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: interest rate swap leg
type: Ontology Class
---

# interest rate swap leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg>

## Definition

swap leg that has an interest rate payment stream, including both a parametric and cashflow representation for the stream of payments

## Relationships

- **Subclass of**: [RateBasedLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/RateBasedLeg.md)

## Constraints

- **[hasBusinessRecurrenceIntervalConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessRecurrenceIntervalConvention.md)**: min qualified cardinality 0 of type [DayCountConvention](/concepts/fibo/FBC/DebtAndEquities/Debt/DayCountConvention.md)
- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: min qualified cardinality 0 of type [NotionalStepSchedule](/concepts/fibo/DER/RateDerivatives/IRSwaps/NotionalStepSchedule.md)
- **[hasPaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule.md)**: min qualified cardinality 0 of type [InterestPaymentSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: min qualified cardinality 0 of type [InterestCalculationSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestCalculationSchedule.md)

## Annotations

- **label**: interest rate swap leg
- **definition**: swap leg that has an interest rate payment stream, including both a parametric and cashflow representation for the stream of payments
- **synonym**: interest rate swap stream

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
