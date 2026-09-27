---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: risk reversal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option trading strategy that consists of being short (selling) an out of the money put and being long (i.e., buying)
      an out of the money call, both with the same maturity
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A risk reversal is a position which simulates profit and loss behavior of owning an underlying security; therefore,
      it is sometimes called a synthetic long. This is an investment strategy that amounts to both buying and selling out-of-money
      options simultaneously. In this strategy, the investor will first make a market hunch; if that hunch is bullish, he
      will want to go long. However, instead of going long on the stock, he will buy an out of the money call option, and
      simultaneously sell an out of the money put option. Presumably he will use the money from the sale of the put option
      to purchase the call option. Then as the stock goes up in price, the call option will be worth more, and the put option
      will be worth less.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/PutOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/RiskReversal
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: risk reversal
type: Ontology Class
---

# risk reversal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/RiskReversal>

## Definition

option trading strategy that consists of being short (selling) an out of the money put and being long (i.e., buying) an out of the money call, both with the same maturity

## Relationships

- **Subclass of**: [OptionTradingStrategy](/concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [CallOption](/concepts/fibo/DER/DerivativesContracts/Options/CallOption.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [PutOption](/concepts/fibo/DER/DerivativesContracts/Options/PutOption.md)

## Annotations

- **label** (en): risk reversal
- **definition** (en): option trading strategy that consists of being short (selling) an out of the money put and being long (i.e., buying) an out of the money call, both with the same maturity
- **explanatoryNote** (en): A risk reversal is a position which simulates profit and loss behavior of owning an underlying security; therefore, it is sometimes called a synthetic long. This is an investment strategy that amounts to both buying and selling out-of-money options simultaneously. In this strategy, the investor will first make a market hunch; if that hunch is bullish, he will want to go long. However, instead of going long on the stock, he will buy an out of the money call option, and simultaneously sell an out of the money put option. Presumably he will use the money from the sale of the put option to purchase the call option. Then as the stock goes up in price, the call option will be worth more, and the put option will be worth less.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
