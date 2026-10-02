---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: notional step change event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event in which a step change in the notional amount for a given swap leg occurs
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The frequency / period length of the steps in the step schedule is a multiple of the calculation period or frequency.
      For example, if the notional is recalculated on every calculation date, applying a new interest rate to the new notional
      amount, then the two frequencies are the same. If notional is updated every second calculation period, then the step
      schedule specifies periods that are twice as long, and so on.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepAmount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/StepEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepEvent
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepChangeEvent
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: notional step change event
type: Ontology Class
---

# notional step change event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepChangeEvent>

## Definition

event in which a step change in the notional amount for a given swap leg occurs

## Relationships

- **Subclass of**: [ContractLifecycleEventOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md)
- **Subclass of**: [StepEvent](/concepts/fibo/SEC/Debt/DebtInstruments/StepEvent.md)

## Constraints

- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: some values from of type [NotionalStepAmount](/concepts/fibo/DER/RateDerivatives/IRSwaps/NotionalStepAmount.md)

## Annotations

- **label**: notional step change event
- **definition**: event in which a step change in the notional amount for a given swap leg occurs
- **explanatoryNote**: The frequency / period length of the steps in the step schedule is a multiple of the calculation period or frequency. For example, if the notional is recalculated on every calculation date, applying a new interest rate to the new notional amount, then the two frequencies are the same. If notional is updated every second calculation period, then the step schedule specifies periods that are twice as long, and so on.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
