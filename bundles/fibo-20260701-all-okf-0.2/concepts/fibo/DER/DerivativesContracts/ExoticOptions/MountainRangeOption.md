---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mountain range option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option based on multiple underlying securities
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Mountain range options are named after a series of mountains, each representing a different type of contract.
      Some of the most common include: (a) Altiplano options: Altiplano options provide investors with the features of both
      a traditional vanilla option along with a coupon payment, (b) Annapurna options: coupon rates are determined by the
      performance of the basket''s worst-performing security when it drops under a specified range, (c) Everest options: Everest
      options place a long-term limit on an investor''s option while offering a payout based on the lagging performers in
      the basket, (d) Atlas options: this type of option eliminates both the best - and worst - performing stocks in a basket
      of securities, and (e) Himalayan options: traders receive a payout based on the basket''s best performing stock; payouts
      are provided on multiple dates.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The price of a mountain range option is based on multiple variables, the most important of which are the correlations
      between the individual securities in the basket. Some options have discrete payout levels, such as double the investment
      or triple the investment, if certain performance metrics are hit by the underlying securities while the option is in
      effect. Mountain range options cannot be priced with standard closed-form approaches. These exotic instruments instead
      require Monte Carlo simulation methods. Effects such as volatility skew, which is found in most options, can be even
      more pronounced within mountain range options.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These options blend some of the key characteristics of basket-style or rainbow options—both of which have more
      than one underlying security or asset—and range options with multiyear time ranges. Prices are based on multiple variables
      - notably the correlations between the individual securities in the basket.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nde9cef5770ab46d397737a1eca595bb8
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/MountainRangeOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: mountain range option
type: Ontology Class
---

# mountain range option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/MountainRangeOption>

## Definition

exotic option based on multiple underlying securities

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nde9cef5770ab46d397737a1eca595bb8`

## Annotations

- **label** (en): mountain range option
- **definition** (en): exotic option based on multiple underlying securities
- **example** (en): Mountain range options are named after a series of mountains, each representing a different type of contract. Some of the most common include: (a) Altiplano options: Altiplano options provide investors with the features of both a traditional vanilla option along with a coupon payment, (b) Annapurna options: coupon rates are determined by the performance of the basket's worst-performing security when it drops under a specified range, (c) Everest options: Everest options place a long-term limit on an investor's option while offering a payout based on the lagging performers in the basket, (d) Atlas options: this type of option eliminates both the best - and worst - performing stocks in a basket of securities, and (e) Himalayan options: traders receive a payout based on the basket's best performing stock; payouts are provided on multiple dates.
- **explanatoryNote** (en): The price of a mountain range option is based on multiple variables, the most important of which are the correlations between the individual securities in the basket. Some options have discrete payout levels, such as double the investment or triple the investment, if certain performance metrics are hit by the underlying securities while the option is in effect. Mountain range options cannot be priced with standard closed-form approaches. These exotic instruments instead require Monte Carlo simulation methods. Effects such as volatility skew, which is found in most options, can be even more pronounced within mountain range options.
- **explanatoryNote** (en): These options blend some of the key characteristics of basket-style or rainbow options—both of which have more than one underlying security or asset—and range options with multiyear time ranges. Prices are based on multiple variables - notably the correlations between the individual securities in the basket.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
