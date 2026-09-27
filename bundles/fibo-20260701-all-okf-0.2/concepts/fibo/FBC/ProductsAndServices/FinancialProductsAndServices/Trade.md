---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trade
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: situation that realizes an agreement between parties participating in a voluntary action of buying and selling
      goods and services
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Deutsche Bank Presentation on the Lifecycle of a Trade, available at http://www.slideshare.net/ahaline/23512555-tradelifecycle
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The advent of money as a medium of exchange has allowed trade to be conducted in a manner that is much simpler
      and effective compared to earlier forms of trade, such as bartering. In financial markets, trading also can mean performing
      a transaction that involves the selling and purchasing of a security.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The seller must deliver the commodity sold to the buyer; the buyer must pay the agreed purchase price, which could
      be in the form of other goods or services, on the agreed date.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Trading activities typically include (a) regularly underwriting or dealing in securities; interest rate, foreign
      exchange rate, commodity, equity, and credit derivative contracts; other financial instruments; and other assets for
      resale, (b) acquiring or taking positions in such items principally for the purpose of selling in the near term or otherwise
      with the intent to resell in order to profit from short-term price movements, and (c) acquiring or taking positions
      in such items as an accommodation to customers or for other trading purposes. (Source: Instructions for Preparation
      of Consolidated Reports of Condition and Income (FFIEC 031 and 041), Schedule RC-D - Trading Assets and Liabilities,
      2013.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isEmbodiedIn
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trader
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isFacilitatedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasBuyer
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Seller
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasSeller
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
    value: Nd9bfe80acafa4a0f85a589dec2d133dd
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/succeeds
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: trade
type: Ontology Class
---

# trade

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade>

## Definition

situation that realizes an agreement between parties participating in a voluntary action of buying and selling goods and services

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[isEmbodiedIn](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/isEmbodiedIn.md)**: some values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **[isFacilitatedBy](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/isFacilitatedBy.md)**: min qualified cardinality 0 of type [Trader](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Trader.md)
- **[hasBuyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/hasBuyer.md)**: some values from of type [Buyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
- **[hasSeller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/hasSeller.md)**: some values from of type [Seller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Seller.md)
- **[involves](/concepts/fibo/FND/Relations/Relations/involves.md)**: some values from value `Nd9bfe80acafa4a0f85a589dec2d133dd`
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: min qualified cardinality 0 of type [TradeLifecycle](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)
- **[succeeds](<https://www.omg.org/spec/Commons/DatesAndTimes/succeeds>)**: min qualified cardinality 0 of type [Trade](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [TradeIdentifier](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md)

## Annotations

- **label**: trade
- **definition**: situation that realizes an agreement between parties participating in a voluntary action of buying and selling goods and services
- **adaptedFrom**: Deutsche Bank Presentation on the Lifecycle of a Trade, available at http://www.slideshare.net/ahaline/23512555-tradelifecycle
- **explanatoryNote**: The advent of money as a medium of exchange has allowed trade to be conducted in a manner that is much simpler and effective compared to earlier forms of trade, such as bartering. In financial markets, trading also can mean performing a transaction that involves the selling and purchasing of a security.
- **explanatoryNote**: The seller must deliver the commodity sold to the buyer; the buyer must pay the agreed purchase price, which could be in the form of other goods or services, on the agreed date.
- **explanatoryNote**: Trading activities typically include (a) regularly underwriting or dealing in securities; interest rate, foreign exchange rate, commodity, equity, and credit derivative contracts; other financial instruments; and other assets for resale, (b) acquiring or taking positions in such items principally for the purpose of selling in the near term or otherwise with the intent to resell in order to profit from short-term price movements, and (c) acquiring or taking positions in such items as an accommodation to customers or for other trading purposes. (Source: Instructions for Preparation of Consolidated Reports of Condition and Income (FFIEC 031 and 041), Schedule RC-D - Trading Assets and Liabilities, 2013.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
