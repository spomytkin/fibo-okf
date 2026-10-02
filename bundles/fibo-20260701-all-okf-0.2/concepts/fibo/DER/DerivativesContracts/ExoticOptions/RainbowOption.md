---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rainbow option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option linked to the performances of two or more underlying assets
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'A best of assets plus cash rainbow effectively has n + 1 payoff possibilities. If we consider a 2 asset "best
      of plus cash", the payoff at expiry is a choice between Asset 1, Asset 2, or the predetermined cash amount. There is
      no strike price and the payoff is given as: Rainbow = max(S1, S2, Cash;T)'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'An asset maximum or minimum payout rainbow is similar to the best of n assets plus cash, with the exception that
      no cash payoff is possible and there is a strike price for this type of option. The payoff of a call and put are given
      as: Rainbow-Call = max[0, max(S1, S2) - X] Rainbow-Put = max[0, X - max(S1, S2)] Minimum of n Assets. The counterpart
      to a maximum of n assets, this rainbow pays out the value of the underperformer of the n assets. The payoff for minimum
      of 2 asset rainbow calls and puts are given as: Rainbow-Call = max[0, mainS1, S2) - X] Rainbow-Put = max[0, X - min(S1,
      S2)]'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Better of n Assets This type of rainbow is similar to the best of n assets plus cash but with the exception that
      there is no possible cash payoff, and X is set to 0. With this in mind, a better of 2 assets rainbow is essentially
      a two-asset call option, with a payoff being: Rainbow = max[0, max(S1, S2)] Worse of n Assets Essentially the opposite
      to the better of n assets, with the payoff being on the asset with the lower value. We can give the payoff for this
      option on 2 assets as: Rainbow = max[0, min(S1, S2)]'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Rainbbow options can speculate on the best performer in the group or minimum performances of all the underlying
      assets at one time. Each underlying may be called a color so the sum of all of these factors makes up a rainbow. These
      structures can be rather exotic and made for institutional clients when referring to financial assets. Rainbow options
      can be structured in many ways depending on how the performances of each underlying asset are considered. Some pay off
      based on the best or worst performance among the underlying assets. In other words, it looks at the top or bottom performance
      and pays off based on that single asset. These are sometimes called 'best of' or 'worst of' rainbow options.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Rainbow options are usually calls or puts on the best or worst of n underlying assets. Like a basket option, which
      is written on a group of assets and pays out on a weighted-average gain on the basket as a whole, a rainbow option also
      considers a group of assets, but usually pays out on the level of one of them. A simple example is a call rainbow option
      written on FTSE 100, Nikkei and S&P 500 which will pay out the difference between the strike price and the level of
      the index that has risen by the largest amount of the three.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N3c08279242a24ffab465ec3953011e2e
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/RainbowOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: rainbow option
type: Ontology Class
---

# rainbow option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/RainbowOption>

## Definition

exotic option linked to the performances of two or more underlying assets

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N3c08279242a24ffab465ec3953011e2e`

## Annotations

- **label** (en): rainbow option
- **definition** (en): exotic option linked to the performances of two or more underlying assets
- **example** (en): A best of assets plus cash rainbow effectively has n + 1 payoff possibilities. If we consider a 2 asset "best of plus cash", the payoff at expiry is a choice between Asset 1, Asset 2, or the predetermined cash amount. There is no strike price and the payoff is given as: Rainbow = max(S1, S2, Cash;T)
- **example** (en): An asset maximum or minimum payout rainbow is similar to the best of n assets plus cash, with the exception that no cash payoff is possible and there is a strike price for this type of option. The payoff of a call and put are given as: Rainbow-Call = max[0, max(S1, S2) - X] Rainbow-Put = max[0, X - max(S1, S2)] Minimum of n Assets. The counterpart to a maximum of n assets, this rainbow pays out the value of the underperformer of the n assets. The payoff for minimum of 2 asset rainbow calls and puts are given as: Rainbow-Call = max[0, mainS1, S2) - X] Rainbow-Put = max[0, X - min(S1, S2)]
- **example** (en): Better of n Assets This type of rainbow is similar to the best of n assets plus cash but with the exception that there is no possible cash payoff, and X is set to 0. With this in mind, a better of 2 assets rainbow is essentially a two-asset call option, with a payoff being: Rainbow = max[0, max(S1, S2)] Worse of n Assets Essentially the opposite to the better of n assets, with the payoff being on the asset with the lower value. We can give the payoff for this option on 2 assets as: Rainbow = max[0, min(S1, S2)]
- **explanatoryNote** (en): Rainbbow options can speculate on the best performer in the group or minimum performances of all the underlying assets at one time. Each underlying may be called a color so the sum of all of these factors makes up a rainbow. These structures can be rather exotic and made for institutional clients when referring to financial assets. Rainbow options can be structured in many ways depending on how the performances of each underlying asset are considered. Some pay off based on the best or worst performance among the underlying assets. In other words, it looks at the top or bottom performance and pays off based on that single asset. These are sometimes called 'best of' or 'worst of' rainbow options.
- **explanatoryNote** (en): Rainbow options are usually calls or puts on the best or worst of n underlying assets. Like a basket option, which is written on a group of assets and pays out on a weighted-average gain on the basket as a whole, a rainbow option also considers a group of assets, but usually pays out on the level of one of them. A simple example is a call rainbow option written on FTSE 100, Nikkei and S&P 500 which will pay out the difference between the strike price and the level of the index that has risen by the largest amount of the three.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
