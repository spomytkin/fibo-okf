---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: floating interest rate leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: floating leg in which variable interest is paid on some notional amount, linked to some underlying interest reference
      rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Instead of an absolute rate you have either a variable reference rate or fixed reference rate and an offset that
      varies in some way, called a spread (same as margin in floating rate notes).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: floating interest rate swap stream
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestCalculationSchedule
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateResetSchedule
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateReset
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/specifies
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateSettingEvent
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/FloatingLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FloatingLeg
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: floating interest rate leg
type: Ontology Class
---

# floating interest rate leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg>

## Definition

floating leg in which variable interest is paid on some notional amount, linked to some underlying interest reference rate

## Relationships

- **Subclass of**: [FloatingLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/FloatingLeg.md)
- **Subclass of**: [InterestRateSwapLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md)

## Constraints

- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: min qualified cardinality 0 of type [InterestCalculationSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestCalculationSchedule.md)
- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: min qualified cardinality 0 of type [InterestRateResetSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestRateResetSchedule.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: min qualified cardinality 0 of type [InterestRateReset](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestRateReset.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: min qualified cardinality 0 of type [InterestRateSettingEvent](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestRateSettingEvent.md)

## Annotations

- **label**: floating interest rate leg
- **definition**: floating leg in which variable interest is paid on some notional amount, linked to some underlying interest reference rate
- **explanatoryNote**: Instead of an absolute rate you have either a variable reference rate or fixed reference rate and an offset that varies in some way, called a spread (same as margin in floating rate notes).
- **synonym**: floating interest rate swap stream

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
