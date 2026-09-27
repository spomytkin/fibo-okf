---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: strip strategy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option trading strategy that involves a sequential set of options with periodic reset dates, such that each period
      between resets behaves like an individual option
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically, a strip is a strategy that involves being long in one call position and two put options, all with the
      same strike price on a single underlying stock. The investor who adopts this strategy believes that the underlying price
      of the stock will plummet in the near-term future. All three of the options will have the same expiration date and the
      same strike price. If the investor is correct and the price drastically decreases, the puts will pay out substantially.
      If the investor is wrong and the price of the underlying asset increases, the call option will mitigate the loss. The
      period between resets may be called a Caplet or Floorlet.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/PutOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StripStrategy
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: strip strategy
type: Ontology Class
---

# strip strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StripStrategy>

## Definition

option trading strategy that involves a sequential set of options with periodic reset dates, such that each period between resets behaves like an individual option

## Relationships

- **Subclass of**: [OptionTradingStrategy](/concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md)

## Constraints

- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: some values from of type [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [CallOption](/concepts/fibo/DER/DerivativesContracts/Options/CallOption.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 2 of type [PutOption](/concepts/fibo/DER/DerivativesContracts/Options/PutOption.md)

## Annotations

- **label** (en): strip strategy
- **definition** (en): option trading strategy that involves a sequential set of options with periodic reset dates, such that each period between resets behaves like an individual option
- **explanatoryNote** (en): Typically, a strip is a strategy that involves being long in one call position and two put options, all with the same strike price on a single underlying stock. The investor who adopts this strategy believes that the underlying price of the stock will plummet in the near-term future. All three of the options will have the same expiration date and the same strike price. If the investor is correct and the price drastically decreases, the puts will pay out substantially. If the investor is wrong and the price of the underlying asset increases, the call option will mitigate the loss. The period between resets may be called a Caplet or Floorlet.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
