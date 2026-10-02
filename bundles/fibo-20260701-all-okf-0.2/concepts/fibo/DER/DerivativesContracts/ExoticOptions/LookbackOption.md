---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lookback option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option that minimizes the uncertainties related to the timing of market entry, providing the holder the
      advantage of knowing history when determining when to exercise their option
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: As a type of exotic option, the lookback allows the user to 'look back,' or review, the prices of an underlying
      asset over the lifespan of the option after it has been purchased. The holder may then exercise the option based on
      the most beneficial price of the underlying asset. The holder can take advantage of the widest differential between
      the strike price and the price of the underlying asset. Lookback options do not trade on major exchanges. Instead, they
      are unlisted and trade over-the-counter (OTC). This type of option reduces uncertainties associated with the timing
      of market entry and reduces the chances the option will expire worthlessly. Lookback options are expensive to execute,
      so these advantages come at a cost.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Lookback options are cash settled options, which means the holder receives a cash settlement at execution based
      on the most advantageous differential between high and low prices during the purchase period. Sellers of lookback options
      would price the option at or near the widest expected distance of price differential based on past volatility and demand
      for the options. The cost to purchase this option would be taken up front. The settlement will equate to the profits
      they could have made from buying or selling the underlying asset. If the settlement was greater than the initial cost
      of the option, then the option buyer would have profit at settlement, otherwise loss.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: lookback option
type: Ontology Class
---

# lookback option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackOption>

## Definition

exotic option that minimizes the uncertainties related to the timing of market entry, providing the holder the advantage of knowing history when determining when to exercise their option

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [LookbackStrikeTerms](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms.md)

## Annotations

- **label** (en): lookback option
- **definition** (en): exotic option that minimizes the uncertainties related to the timing of market entry, providing the holder the advantage of knowing history when determining when to exercise their option
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): As a type of exotic option, the lookback allows the user to 'look back,' or review, the prices of an underlying asset over the lifespan of the option after it has been purchased. The holder may then exercise the option based on the most beneficial price of the underlying asset. The holder can take advantage of the widest differential between the strike price and the price of the underlying asset. Lookback options do not trade on major exchanges. Instead, they are unlisted and trade over-the-counter (OTC). This type of option reduces uncertainties associated with the timing of market entry and reduces the chances the option will expire worthlessly. Lookback options are expensive to execute, so these advantages come at a cost.
- **explanatoryNote** (en): Lookback options are cash settled options, which means the holder receives a cash settlement at execution based on the most advantageous differential between high and low prices during the purchase period. Sellers of lookback options would price the option at or near the widest expected distance of price differential based on past volatility and demand for the options. The cost to purchase this option would be taken up front. The settlement will equate to the profits they could have made from buying or selling the underlying asset. If the settlement was greater than the initial cost of the option, then the option buyer would have profit at settlement, otherwise loss.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
