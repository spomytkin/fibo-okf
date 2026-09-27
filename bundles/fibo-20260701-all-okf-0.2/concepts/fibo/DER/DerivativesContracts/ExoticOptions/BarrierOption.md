---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: barrier option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option whose final exercise depends upon the path taken by the price of an underlying instrument, i.e., whose payoff
      depends on whether or not the underlying asset has reached or exceeded a predetermined price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: For a knock-out barrier option, the option is cancelled if the underlying price crosses a predetermined barrier
      level; for a knock-in barrier option, the option becomes available-for-exercise if the underlying price crosses a predetermined
      barrier level.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A barrier option can be a knock-out, meaning it expires worthless if the underlying exceeds a certain price, limiting
      profits for the holder and limiting losses for the writer. It can also be a knock-in, meaning it has no value until
      the underlying reaches a certain price. Barrier options can be puts or calls. Barrier options typically have cheaper
      premiums than traditional vanilla options, primarily because the barrier increases the chances of the option expiring
      worthless. A trader may choose the cheaper (relative to a comparable vanilla) barrier option if they feel it is quite
      likely the underlying will hit the barrier.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Barrier features include any terms related to exercising the option ahead of the expiry date.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#positiveInteger
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasMonitoringFrequency
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasMonitoringPeriod
  - filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/isAboveStrikePrice
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: barrier option
type: Ontology Class
---

# barrier option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption>

## Definition

option whose final exercise depends upon the path taken by the price of an underlying instrument, i.e., whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasMonitoringFrequency](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasMonitoringFrequency.md)**: some values from of type [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)
- **[hasMonitoringPeriod](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasMonitoringPeriod.md)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[isAboveStrikePrice](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/isAboveStrikePrice.md)**: some values from of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): barrier option
- **definition** (en): option whose final exercise depends upon the path taken by the price of an underlying instrument, i.e., whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price
- **note** (en): For a knock-out barrier option, the option is cancelled if the underlying price crosses a predetermined barrier level; for a knock-in barrier option, the option becomes available-for-exercise if the underlying price crosses a predetermined barrier level.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): A barrier option can be a knock-out, meaning it expires worthless if the underlying exceeds a certain price, limiting profits for the holder and limiting losses for the writer. It can also be a knock-in, meaning it has no value until the underlying reaches a certain price. Barrier options can be puts or calls. Barrier options typically have cheaper premiums than traditional vanilla options, primarily because the barrier increases the chances of the option expiring worthless. A trader may choose the cheaper (relative to a comparable vanilla) barrier option if they feel it is quite likely the underlying will hit the barrier.
- **explanatoryNote** (en): Barrier features include any terms related to exercising the option ahead of the expiry date.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
